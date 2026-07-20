#!/usr/bin/env python3
"""Validate the static course project without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "Anthropic工程博客学习路径课程.html"
CLASSIFICATION = (
    ROOT
    / "anthropic-engineering-crawl"
    / "anthropic_engineering_articles_classification.html"
)
TRANSLATIONS = (
    ROOT
    / "anthropic-engineering-crawl"
    / "anthropic_engineering_articles_zh.html"
)
FULLTEXT = (
    ROOT
    / "anthropic-engineering-crawl"
    / "anthropic_engineering_articles_fulltext.json"
)
AUDIT_REPORT = ROOT / "教育审查与优化报告.md"
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


def local_link_errors(path: Path, hrefs: list[str]) -> list[str]:
    errors: list[str] = []
    for href in hrefs:
        if not href or href.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = unquote(href.split("#", 1)[0])
        if target and not (path.parent / target).exists():
            errors.append(f"{path.name}: missing local link {href}")
    return errors


def expect_equal(errors: list[str], label: str, actual: int, expected: int) -> None:
    if actual != expected:
        errors.append(f"{label}: expected {expected}, found {actual}")


def main() -> int:
    errors: list[str] = []
    required = [
        COURSE,
        CLASSIFICATION,
        TRANSLATIONS,
        ROOT / "AGENTS.md",
        ROOT / "MEMORY.md",
        AUDIT_REPORT,
        FULLTEXT,
        ROOT / "agent" / "feature_list.md",
        ROOT / "agent" / "memory" / "article_stage_map.md",
        ROOT / "课程学习工作区模板.zip",
        ROOT / "课程学习工作区模板" / "开始这里.txt",
        ROOT / "课程学习工作区模板" / "notes" / "阶段学习笔记.txt",
        ROOT / "课程学习工作区模板" / "outputs" / "阶段产出记录.txt",
        ROOT / "课程学习工作区模板" / "questions" / "待解决问题.txt",
        ROOT / "课程学习工作区模板" / "project" / "预约管理平台案例.txt",
        ROOT / "课程学习工作区模板" / "prompts" / "AI学习助教提示词.txt",
        *[
            ROOT / "课程学习工作区模板" / "outputs" / template
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
    classification_text, classification = parse(CLASSIFICATION)
    translation_text, translations = parse(TRANSLATIONS)
    audit_report_text = AUDIT_REPORT.read_text(encoding="utf-8")
    fulltext_data = json.loads(FULLTEXT.read_text(encoding="utf-8"))

    for path, parser in (
        (COURSE, course),
        (CLASSIFICATION, classification),
        (TRANSLATIONS, translations),
    ):
        duplicates = duplicate_values(parser.ids)
        if duplicates:
            errors.append(f"{path.name}: duplicate ids {', '.join(duplicates)}")
        errors.extend(local_link_errors(path, parser.hrefs))

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

    translation_slugs = re.findall(
        r'^\s+slug:\s*"([^"]+)"', translation_text, flags=re.MULTILINE
    )
    expect_equal(errors, "Chinese reading summaries", len(translation_slugs), 25)

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

    course_translation_links = re.findall(
        r'href="anthropic-engineering-crawl/'
        r'anthropic_engineering_articles_zh\.html#([^"]+)"',
        course_text,
    )
    expect_equal(errors, "course Chinese summary links", len(course_translation_links), 25)
    unknown_translation_links = sorted(
        set(course_translation_links) - set(translation_slugs)
    )
    if unknown_translation_links:
        errors.append(
            "course links to missing Chinese summaries: "
            + ", ".join(unknown_translation_links)
        )

    classification_translation_links = re.findall(
        r'href="anthropic_engineering_articles_zh\.html#([^"]+)"',
        classification_text,
    )
    expect_equal(
        errors,
        "classification Chinese summary links",
        len(classification_translation_links),
        25,
    )
    unknown_classification_links = sorted(
        set(classification_translation_links) - set(translation_slugs)
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

    if "nextLabelForInput" not in course_text or "scrollIntoView" not in course_text:
        errors.append("continue-learning direct navigation is missing")

    if "data-complete-progress" not in course_text or "prepContinue.hidden" not in course_text:
        errors.append("guided course setup actions are missing")

    if "完成本页，不等于已经完成生产产品" not in course_text:
        errors.append("prerequisite and production-course boundary is missing")

    if "不是逐段或完整翻译" not in translation_text:
        errors.append("Chinese summary coverage disclosure is missing")

    if (
        'id="articleDrawer"' not in course_text
        or "openArticleDrawer" not in course_text
        or "?embed=1#" not in course_text
    ):
        errors.append("in-course Chinese summary drawer is missing")

    if 'data-filter="all"' not in classification_text:
        errors.append("classification filter controls are missing")

    if "renderArticle" not in translation_text or "articleSearch" not in translation_text:
        errors.append("Chinese summary reader navigation is missing")

    if 'classList.add("embed")' not in translation_text:
        errors.append("Chinese summary embedded drawer mode is missing")

    course_target_block = re.search(
        r"const courseTargets = \{(.*?)\n\s*\};",
        translation_text,
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
        missing_targets = sorted(set(translation_slugs) - mapped_slugs)
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
    print(f"- Chinese reading summaries: {len(translation_slugs)}")
    print(f"- audited article titles: {len(article_titles)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
