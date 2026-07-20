#!/usr/bin/env python3
"""Validate the static course project without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "course" / "index.html"
COURSE_SCRIPT = ROOT / "course" / "assets" / "course.js"
CLASSIFICATION = ROOT / "course" / "articles" / "classification.html"
CLASSIFICATION_SCRIPT = ROOT / "course" / "assets" / "classification.js"
READING_SUMMARIES = ROOT / "course" / "articles" / "reader.html"
READING_SUMMARIES_SCRIPT = ROOT / "course" / "assets" / "reader.js"
FULLTEXT = ROOT / "content" / "sources" / "anthropic" / "articles-fulltext.json"
AUDIT_REPORT = ROOT / "content" / "curriculum" / "education-audit.zh-CN.md"
WORKSPACE = ROOT / "materials" / "learner-workspace"
LEGACY_ENTRIES = {
    ROOT / "index.html": "course/index.html",
    ROOT / "Anthropic工程博客学习路径课程.html": "course/index.html",
    ROOT
    / "anthropic-engineering-crawl"
    / "anthropic_engineering_articles_classification.html": (
        "../course/articles/classification.html"
    ),
    ROOT / "anthropic-engineering-crawl" / "anthropic_engineering_articles_zh.html": (
        "../course/articles/reader.html"
    ),
}
STAGE_TEMPLATES = [
    "阶段1-Agent执行流程与概念说明.md",
    "阶段2-产品规格与进度控制.md",
    "阶段3-工具与上下文边界.md",
    "阶段4-安全边界与权限矩阵.md",
    "阶段5-评测用例与证据规则.md",
    "阶段6-故障处理与复盘.md",
]


class ProjectHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.hrefs: list[str] = []
        self.srcs: list[str] = []
        self.classes: list[set[str]] = []
        self.attributes: list[dict[str, str]] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        values = {key: value or "" for key, value in attrs}
        self.attributes.append(values)
        if values.get("id"):
            self.ids.append(values["id"])
        if values.get("href"):
            self.hrefs.append(values["href"])
        if values.get("src"):
            self.srcs.append(values["src"])
        self.classes.append(set(values.get("class", "").split()))

    def class_count(self, class_name: str) -> int:
        return sum(class_name in classes for classes in self.classes)

    def attribute_count(self, name: str) -> int:
        return sum(name in attributes for attributes in self.attributes)


def parse(path: Path) -> tuple[str, ProjectHTMLParser]:
    text = path.read_text(encoding="utf-8")
    parser = ProjectHTMLParser()
    parser.feed(text)
    return text, parser


def duplicate_values(values: list[str]) -> list[str]:
    return sorted({value for value in values if values.count(value) > 1})


def local_link_errors(path: Path, references: list[str]) -> list[str]:
    errors: list[str] = []
    for reference in references:
        if not reference or reference.startswith(
            ("#", "http://", "https://", "mailto:", "about:")
        ):
            continue
        target = unquote(reference.split("#", 1)[0])
        if target and not (path.parent / target).exists():
            errors.append(f"{path.name}: missing local resource {reference}")
    return errors


def expect_equal(errors: list[str], label: str, actual: int, expected: int) -> None:
    if actual != expected:
        errors.append(f"{label}: expected {expected}, found {actual}")


def main() -> int:
    errors: list[str] = []
    required = [
        COURSE,
        COURSE_SCRIPT,
        ROOT / "course" / "assets" / "course.css",
        CLASSIFICATION,
        CLASSIFICATION_SCRIPT,
        ROOT / "course" / "assets" / "classification.css",
        READING_SUMMARIES,
        READING_SUMMARIES_SCRIPT,
        ROOT / "course" / "assets" / "reader.css",
        ROOT / "AGENTS.md",
        ROOT / "MEMORY.md",
        ROOT / "README.md",
        *LEGACY_ENTRIES,
        ROOT / "docs" / "architecture.md",
        ROOT / "scripts" / "check-js-syntax.mjs",
        ROOT / "scripts" / "package_materials.py",
        AUDIT_REPORT,
        FULLTEXT,
        ROOT / "agent" / "feature_list.md",
        ROOT / "agent" / "memory" / "article_stage_map.md",
        ROOT / "materials" / "learner-workspace.zip",
        WORKSPACE / "开始这里.txt",
        WORKSPACE / "notes" / "阶段学习笔记.txt",
        WORKSPACE / "outputs" / "阶段产出记录.txt",
        WORKSPACE / "questions" / "待解决问题.txt",
        WORKSPACE / "project" / "预约管理平台案例.txt",
        WORKSPACE / "prompts" / "AI学习助教提示词.txt",
        *[
            WORKSPACE / "outputs" / template
            for template in STAGE_TEMPLATES
        ],
    ]
    for path in required:
        if not path.exists():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1

    course_text, course = parse(COURSE)
    course_script_text = COURSE_SCRIPT.read_text(encoding="utf-8")
    classification_text, classification = parse(CLASSIFICATION)
    classification_script_text = CLASSIFICATION_SCRIPT.read_text(encoding="utf-8")
    reading_summary_text, reading_summaries = parse(READING_SUMMARIES)
    reading_summary_script_text = READING_SUMMARIES_SCRIPT.read_text(encoding="utf-8")
    audit_report_text = AUDIT_REPORT.read_text(encoding="utf-8")
    fulltext_data = json.loads(FULLTEXT.read_text(encoding="utf-8"))

    for path, parser in (
        (COURSE, course),
        (CLASSIFICATION, classification),
        (READING_SUMMARIES, reading_summaries),
    ):
        duplicates = duplicate_values(parser.ids)
        if duplicates:
            errors.append(f"{path.name}: duplicate ids {', '.join(duplicates)}")
        errors.extend(local_link_errors(path, parser.hrefs + parser.srcs))

    for path, expected_target in LEGACY_ENTRIES.items():
        redirect_text, redirect_page = parse(path)
        errors.extend(
            local_link_errors(path, redirect_page.hrefs + redirect_page.srcs)
        )
        if f'url={expected_target}' not in redirect_text:
            errors.append(
                f"{path.relative_to(ROOT)}: missing redirect to {expected_target}"
            )
        if f"`{expected_target}${{location.hash}}`" not in redirect_text:
            errors.append(
                f"{path.relative_to(ROOT)}: redirect does not preserve URL hash"
            )

    for path, text in (
        (COURSE, course_text),
        (CLASSIFICATION, classification_text),
        (READING_SUMMARIES, reading_summary_text),
    ):
        if "<style" in text:
            errors.append(f"{path.name}: inline style block should live in course/assets")
        expect_equal(
            errors,
            f"{path.name} external scripts",
            len(re.findall(r"<script\s+src=", text)),
            1,
        )

    expect_equal(errors, "learning stages", course.class_count("learning-stage"), 6)
    expect_equal(errors, "required article units", course.class_count("article-unit"), 12)
    expect_equal(errors, "knowledge checks", course.class_count("knowledge-check"), 6)
    expect_equal(errors, "lesson loops", course.class_count("lesson-loop"), 6)
    expect_equal(errors, "worked examples", course.class_count("worked-example"), 6)
    expect_equal(errors, "chapter prequestions", course.class_count("chapter-prequestion"), 6)
    expect_equal(errors, "chapter concept sequences", course.class_count("concept-sequence"), 6)
    expect_equal(errors, "chapter concept items", course.class_count("concept-item"), 30)
    expect_equal(errors, "article guide blocks", course.class_count("guide-block"), 60)
    expect_equal(errors, "self-explanation prompts", course.class_count("self-explain"), 6)
    expect_equal(errors, "spaced reviews", course.class_count("spaced-review"), 6)
    expect_equal(errors, "guided practices", course.class_count("guided-practice"), 6)
    expect_equal(errors, "stage template links", course.class_count("template-link"), 6)
    expect_equal(errors, "learning model steps", course.class_count("learning-model-row"), 6)
    expect_equal(errors, "prepared setup actions", course.class_count("setup-item"), 5)
    expect_equal(errors, "persistent reflections", course.attribute_count("data-reflection"), 18)
    expect_equal(errors, "delayed review checks", course.attribute_count("data-review"), 6)
    expect_equal(errors, "assessment dimensions", course.class_count("rubric-dimension"), 5)
    expect_equal(errors, "full-stack milestones", course.class_count("bridge-row"), 8)
    expect_equal(errors, "classification articles", classification.class_count("article"), 25)

    reading_summary_slugs = re.findall(
        r'^\s+slug:\s*"([^"]+)"',
        reading_summary_script_text,
        flags=re.MULTILINE,
    )
    expect_equal(errors, "Chinese reading summaries", len(reading_summary_slugs), 25)

    article_titles = [
        article.get("title", "") for article in fulltext_data.get("articles", [])
    ]
    expect_equal(errors, "archived full-text articles", len(article_titles), 25)
    missing_audit_articles = [
        title for title in article_titles if title and title not in audit_report_text
    ]
    if missing_audit_articles:
        errors.append(
            "audit report is missing articles: " + ", ".join(missing_audit_articles)
        )

    course_summary_links = re.findall(
        r'href="articles/reader\.html#([^"]+)"',
        course_text,
    )
    expect_equal(errors, "course Chinese summary links", len(course_summary_links), 25)
    unknown_summary_links = sorted(
        set(course_summary_links) - set(reading_summary_slugs)
    )
    if unknown_summary_links:
        errors.append(
            "course links to missing Chinese summaries: "
            + ", ".join(unknown_summary_links)
        )

    classification_summary_links = re.findall(
        r'href="reader\.html#([^"]+)"',
        classification_text,
    )
    expect_equal(
        errors,
        "classification Chinese summary links",
        len(classification_summary_links),
        25,
    )
    unknown_classification_links = sorted(
        set(classification_summary_links) - set(reading_summary_slugs)
    )
    if unknown_classification_links:
        errors.append(
            "classification links to missing Chinese summaries: "
            + ", ".join(unknown_classification_links)
        )

    quiz_answers = len(re.findall(r'data-quiz="[^"]+"\s+data-answer="[^"]+"', course_text))
    expect_equal(errors, "quiz answer keys", quiz_answers, 6)

    if re.search(r'data-progress="stage-[1-6]-read"', course_text):
        errors.append("generic stage reading checkboxes still exist")

    if (
        "nextLabelForInput" not in course_script_text
        or "scrollIntoView" not in course_script_text
    ):
        errors.append("continue-learning direct navigation is missing")

    if (
        "data-complete-progress" not in course_text
        or "prepContinue.hidden" not in course_script_text
    ):
        errors.append("guided course setup actions are missing")

    if "完成本页，不等于已经完成生产产品" not in course_text:
        errors.append("prerequisite and production-course boundary is missing")

    if "不是逐段或完整翻译" not in reading_summary_text:
        errors.append("Chinese summary coverage disclosure is missing")

    if (
        'id="articleDrawer"' not in course_text
        or "openArticleDrawer" not in course_script_text
        or "?embed=1#" not in course_script_text
    ):
        errors.append("in-course Chinese summary drawer is missing")

    if 'data-filter="all"' not in classification_text:
        errors.append("classification filter controls are missing")

    if (
        "renderArticle" not in reading_summary_script_text
        or "articleSearch" not in reading_summary_script_text
    ):
        errors.append("Chinese summary reader navigation is missing")

    if 'classList.add("embed")' not in reading_summary_script_text:
        errors.append("Chinese summary embedded drawer mode is missing")

    if "applyFilter" not in classification_script_text:
        errors.append("classification filtering logic is missing")

    course_target_block = re.search(
        r"const courseTargets = \{(.*?)\n\s*\};",
        reading_summary_script_text,
        flags=re.DOTALL,
    )
    if not course_target_block:
        errors.append("Chinese summary return-to-course map is missing")
    else:
        course_target_pairs = re.findall(
            r'^\s*"([^"]+)":\s*"([^"]+)"',
            course_target_block.group(1),
            flags=re.MULTILINE,
        )
        expect_equal(
            errors,
            "Chinese summary course return targets",
            len(course_target_pairs),
            25,
        )
        mapped_slugs = {slug for slug, _ in course_target_pairs}
        missing_targets = sorted(set(reading_summary_slugs) - mapped_slugs)
        if missing_targets:
            errors.append(
                "Chinese summaries missing course return targets: "
                + ", ".join(missing_targets)
            )
        missing_course_ids = sorted(
            target for _, target in course_target_pairs if target not in course.ids
        )
        if missing_course_ids:
            errors.append(
                "Chinese summary return targets missing in course: "
                + ", ".join(missing_course_ids)
            )

    if errors:
        print("Project validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    workspace_files = sorted(
        str(Path("learner-workspace") / path.relative_to(WORKSPACE))
        for path in WORKSPACE.rglob("*")
        if path.is_file()
    )
    with ZipFile(ROOT / "materials" / "learner-workspace.zip") as archive:
        archived_files = sorted(
            name
            for name in archive.namelist()
            if not name.endswith("/") and not name.startswith("__MACOSX/")
        )
    if archived_files != workspace_files:
        print("Project validation failed:")
        print("- learner workspace ZIP does not match materials/learner-workspace")
        return 1

    progress_items = course.attribute_count("data-progress")
    external_course_links = sum(
        href.startswith(("http://", "https://")) for href in course.hrefs
    )
    print("Project validation passed")
    print(f"- learning stages: {course.class_count('learning-stage')}")
    print(f"- required article units: {course.class_count('article-unit')}")
    print(f"- knowledge checks: {course.class_count('knowledge-check')}")
    print(f"- chapter concept items: {course.class_count('concept-item')}")
    print(f"- article guide blocks: {course.class_count('guide-block')}")
    print(f"- spaced reviews: {course.class_count('spaced-review')}")
    print(f"- guided practices: {course.class_count('guided-practice')}")
    print(f"- persistent reflections: {course.attribute_count('data-reflection')}")
    print(f"- delayed review checks: {course.attribute_count('data-review')}")
    print(f"- assessment dimensions: {course.class_count('rubric-dimension')}")
    print(f"- full-stack milestones: {course.class_count('bridge-row')}")
    print(f"- progress items: {progress_items}")
    print(f"- course external links: {external_course_links}")
    print(f"- classification articles: {classification.class_count('article')}")
    print(f"- Chinese reading summaries: {len(reading_summary_slugs)}")
    print(f"- audited article titles: {len(article_titles)}")
    print(f"- learner workspace files: {len(workspace_files)}")
    print(f"- compatibility entries: {len(LEGACY_ENTRIES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
