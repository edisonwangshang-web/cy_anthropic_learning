    (() => {
      const storageKey = "anthropic-engineering-course-progress-v2";
      const reflectionStorageKey = "anthropic-engineering-course-reflections-v1";
      const reviewStorageKey = "anthropic-engineering-course-reviews-v1";
      const progressInputs = Array.from(document.querySelectorAll("[data-progress]"));
      const reflectionInputs = Array.from(document.querySelectorAll("[data-reflection]"));
      const reviewInputs = Array.from(document.querySelectorAll("[data-review]"));
      const progressValue = document.getElementById("progressValue");
      const progressFill = document.getElementById("progressFill");
      const progressTrack = document.getElementById("progressTrack");
      const progressCopy = document.getElementById("progressCopy");
      const reviewCopy = document.getElementById("reviewCopy");
      const mobileProgressValue = document.getElementById("mobileProgressValue");
      const mobileProgressFill = document.getElementById("mobileProgressFill");
      const mobileProgressTrack = document.getElementById("mobileProgressTrack");
      const nextTask = document.getElementById("nextTask");
      const heroContinue = document.getElementById("heroContinue");
      const topContinue = document.getElementById("topContinue");
      const readyState = document.getElementById("readyState");
      const prepContinue = document.getElementById("prepContinue");
      const articleDrawer = document.getElementById("articleDrawer");
      const drawerFrame = document.getElementById("drawerFrame");
      const drawerTitle = document.getElementById("drawerTitle");
      const drawerContext = document.getElementById("drawerContext");
      const drawerClose = document.getElementById("drawerClose");
      let drawerTrigger = null;

      const closeArticleDrawer = () => {
        if (articleDrawer.hidden) return;
        articleDrawer.hidden = true;
        document.body.classList.remove("drawer-open");
        drawerFrame.src = "about:blank";
        if (drawerTrigger) drawerTrigger.focus();
      };

      const openArticleDrawer = (link) => {
        const href = link.getAttribute("href");
        const [readerPath, slug] = href.split("#");
        if (!readerPath || !slug) return;

        const article = link.closest(".article-unit");
        const stage = link.closest(".learning-stage");
        const articleName = article?.querySelector(".article-title")?.textContent
          || link.textContent.trim();
        const stageName = stage?.querySelector(".stage-header h3")?.textContent;

        drawerTrigger = link;
        drawerTitle.textContent = articleName;
        drawerFrame.title = `${articleName}中文精读摘要`;
        drawerFrame.src = `${readerPath}?embed=1#${slug}`;
        drawerContext.textContent = stageName
          ? `读完后返回“${stageName}”，继续完成阅读问题和即时回忆。`
          : "读完后关闭抽屉，回到当前课程任务。";
        articleDrawer.hidden = false;
        document.body.classList.add("drawer-open");
        window.requestAnimationFrame(() => drawerClose.focus());
      };

      document.querySelectorAll('a[href*="articles/reader.html#"]').forEach((link) => {
        link.addEventListener("click", (event) => {
          if (
            event.button !== 0
            || event.metaKey
            || event.ctrlKey
            || event.shiftKey
            || event.altKey
          ) return;
          event.preventDefault();
          openArticleDrawer(link);
        });
      });

      document.querySelectorAll("[data-close-drawer]").forEach((control) => {
        control.addEventListener("click", closeArticleDrawer);
      });

      document.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && !articleDrawer.hidden) {
          closeArticleDrawer();
        }
      });

      window.addEventListener("message", (event) => {
        if (event.data?.type === "close-article-drawer") {
          closeArticleDrawer();
        }
      });

      const readState = () => {
        try {
          return JSON.parse(localStorage.getItem(storageKey) || "{}");
        } catch {
          return {};
        }
      };

      const writeState = () => {
        const state = {};
        progressInputs.forEach((input) => {
          state[input.dataset.progress] = input.checked;
        });
        localStorage.setItem(storageKey, JSON.stringify(state));
      };

      const readStorageObject = (key) => {
        try {
          return JSON.parse(localStorage.getItem(key) || "{}");
        } catch {
          return {};
        }
      };

      const writeReflectionState = () => {
        const state = {};
        reflectionInputs.forEach((input) => {
          state[input.dataset.reflection] = input.value;
        });
        localStorage.setItem(reflectionStorageKey, JSON.stringify(state));
      };

      const writeReviewState = () => {
        const state = {};
        reviewInputs.forEach((input) => {
          state[input.dataset.review] = input.checked;
        });
        localStorage.setItem(reviewStorageKey, JSON.stringify(state));
      };

      const updateReviewStatus = () => {
        const completed = reviewInputs.filter((input) => input.checked).length;
        reviewCopy.textContent = `延迟复习 ${completed} / ${reviewInputs.length}`;
      };

      const stageForInput = (input) => input.closest(".learning-stage");

      const nextLabelForInput = (input) => {
        const article = input.closest(".article-unit");
        if (article) {
          const title = article.querySelector(".article-title");
          return title ? `完成《${title.textContent}》导读与阅读问题` : "完成文章导读";
        }
        const quiz = input.closest(".knowledge-check");
        if (quiz) {
          const stage = quiz.closest(".learning-stage");
          const title = stage ? stage.querySelector(".stage-header h3") : null;
          return title ? `通过“${title.textContent}”即时回忆` : "通过即时回忆";
        }
        const label = input.closest(".check-item");
        const strong = label ? label.querySelector("strong") : null;
        return strong ? strong.textContent : "继续下一项学习任务";
      };

      const updateReadyState = () => {
        const prepInputs = Array.from(document.querySelectorAll("#prepChecklist [data-progress]"));
        const ready = prepInputs.every((input) => input.checked);
        const remaining = prepInputs.filter((input) => !input.checked).length;
        readyState.textContent = ready
          ? "开课设置完成。下一步只做阶段 1 的第一篇文章导读。"
          : `还剩 ${remaining} 个动作。按编号继续，内容和模板都已经准备好。`;
        readyState.classList.toggle("is-ready", ready);
        prepContinue.hidden = !ready;
      };

      const updateArticleStates = () => {
        document.querySelectorAll(".article-unit").forEach((article) => {
          const input = article.querySelector("[data-progress]");
          const type = article.querySelector(".reading-type");
          if (!input || !type) return;
          type.textContent = input.checked ? "完成" : "必读";
        });
      };

      const updateProgress = () => {
        const completed = progressInputs.filter((input) => input.checked).length;
        const total = progressInputs.length;
        const percent = total ? Math.round((completed / total) * 100) : 0;
        const firstIncomplete = progressInputs.find((input) => !input.checked);
        const stage = firstIncomplete ? stageForInput(firstIncomplete) : null;
        const target = stage ? `#${stage.id}` : firstIncomplete ? "#prepare" : "#assessment";
        const nextText = firstIncomplete ? nextLabelForInput(firstIncomplete) : "课程任务已全部完成，进入最终复核";

        progressValue.textContent = `${percent}%`;
        progressFill.style.width = `${percent}%`;
        progressTrack.setAttribute("aria-valuenow", String(percent));
        progressCopy.textContent = `已完成 ${completed} / ${total} 项`;
        mobileProgressValue.textContent = `${percent}%`;
        mobileProgressFill.style.width = `${percent}%`;
        mobileProgressTrack.setAttribute("aria-valuenow", String(percent));
        nextTask.textContent = nextText;
        heroContinue.href = target;
        topContinue.href = target;
        heroContinue.textContent = completed ? "从下一项继续" : "从第一项开始";

        updateReadyState();
        updateArticleStates();
      };

      const savedState = readState();
      progressInputs.forEach((input) => {
        input.checked = Boolean(savedState[input.dataset.progress]);
        input.addEventListener("change", () => {
          writeState();
          updateProgress();
        });
      });

      const savedReflections = readStorageObject(reflectionStorageKey);
      reflectionInputs.forEach((input) => {
        input.value = savedReflections[input.dataset.reflection] || "";
        input.addEventListener("input", writeReflectionState);
      });

      const savedReviews = readStorageObject(reviewStorageKey);
      reviewInputs.forEach((input) => {
        input.checked = Boolean(savedReviews[input.dataset.review]);
        input.addEventListener("change", () => {
          writeReviewState();
          updateReviewStatus();
        });
      });

      document.querySelectorAll("[data-complete-progress]").forEach((control) => {
        control.addEventListener("click", () => {
          const key = control.dataset.completeProgress;
          const input = progressInputs.find((candidate) => candidate.dataset.progress === key);
          if (!input) return;
          input.checked = true;
          writeState();
          updateProgress();
        });
      });

      document.querySelectorAll("[data-quiz]").forEach((quiz) => {
        const submit = quiz.querySelector(".quiz-submit");
        const feedback = quiz.querySelector(".quiz-feedback");
        const mastery = quiz.querySelector(".mastery-check [data-progress]");
        const correctAnswer = quiz.dataset.answer;
        const feedbackByStage = {
          "stage-1": {
            correct: "回答正确。固定规则由 Workflow 承担，只把自然语言分类交给 AI，并在后面接确定性校验。",
            wrong: "回看“Workflow 与 Agent”和“反馈与停止条件”。本题规则、顺序和退款权限都已确定，不需要全自主 Agent。"
          },
          "stage-2": {
            correct: "回答正确。跨用户测试、接口结果和日志共同证明权限规则，而不是只证明页面能打开。",
            wrong: "回看“证据闭环”。自己的页面可用只能证明正常路径，不能证明其他账号无法越权访问。"
          },
          "stage-3": {
            correct: "回答正确。实时业务数据应通过受限只读工具获取，并限制字段、范围和失败状态。",
            wrong: "回看“工具是一份契约”和“数据暴露”。每天变化的数据不能靠旧提示词或让 AI 猜测。"
          },
          "stage-4": {
            correct: "回答正确。独立测试数据库把破坏范围限制在可重建环境，比反复弹窗更可靠。",
            wrong: "回看“三环境隔离”和“提示确认与真正边界”。生产密钥和生产数据不应进入开发测试。"
          },
          "stage-5": {
            correct: "回答正确。先固定环境并重复运行，再比较轨迹、资源和失败位置，才能解释波动。",
            wrong: "回看“基础设施噪声”和“重复与回归”。单次结果不足以证明模型退化或系统稳定。"
          },
          "stage-6": {
            correct: "回答正确。先确认时间和范围，再检查最近变更与全链路证据，症状不能直接当根因。",
            wrong: "回看“症状不等于根因”和“先建立事实边界”。先改提示词会破坏现场，也无法证明原因。"
          }
        };
        const stageFeedback = feedbackByStage[quiz.dataset.quiz];

        if (mastery.checked) {
          feedback.textContent = "已通过。你可以继续完成示例和项目产出。";
          feedback.classList.add("is-correct");
        }

        submit.addEventListener("click", () => {
          const selected = quiz.querySelector("input[type='radio']:checked");
          feedback.classList.remove("is-correct", "is-wrong");

          if (!selected) {
            feedback.textContent = "请先选择一个答案。";
            feedback.classList.add("is-wrong");
            return;
          }

          if (selected.value === correctAnswer) {
            mastery.checked = true;
            feedback.textContent = stageFeedback.correct;
            feedback.classList.add("is-correct");
            writeState();
            updateProgress();
          } else {
            feedback.textContent = stageFeedback.wrong;
            feedback.classList.add("is-wrong");
          }
        });
      });

      document.getElementById("resetProgress").addEventListener("click", () => {
        const confirmed = window.confirm("确定要清除这门课的全部学习进度吗？");
        if (!confirmed) return;
        progressInputs.forEach((input) => {
          input.checked = false;
        });
        reviewInputs.forEach((input) => {
          input.checked = false;
        });
        reflectionInputs.forEach((input) => {
          input.value = "";
        });
        document.querySelectorAll(".quiz-feedback").forEach((feedback) => {
          feedback.textContent = "";
          feedback.classList.remove("is-correct", "is-wrong");
        });
        localStorage.removeItem(storageKey);
        localStorage.removeItem(reviewStorageKey);
        localStorage.removeItem(reflectionStorageKey);
        updateReviewStatus();
        updateProgress();
      });

      [heroContinue, topContinue].forEach((link) => {
        link.addEventListener("click", (event) => {
          const firstIncomplete = progressInputs.find((input) => !input.checked);
          if (!firstIncomplete) return;
          const articleDetails = firstIncomplete.closest(".article-unit")?.querySelector("details");
          const target = articleDetails
            || firstIncomplete.closest(".knowledge-check")
            || firstIncomplete.closest(".check-item")
            || firstIncomplete.closest(".learning-stage");
          if (!target) return;
          event.preventDefault();
          if (articleDetails) articleDetails.open = true;
          target.scrollIntoView({ behavior: "smooth", block: "center" });
        });
      });

      document.querySelectorAll("[data-copy-target]").forEach((button) => {
        button.addEventListener("click", async () => {
          const target = document.getElementById(button.dataset.copyTarget);
          const text = target.textContent.trim();
          try {
            await navigator.clipboard.writeText(text);
          } catch {
            const textarea = document.createElement("textarea");
            textarea.value = text;
            textarea.setAttribute("readonly", "");
            textarea.style.position = "fixed";
            textarea.style.opacity = "0";
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand("copy");
            textarea.remove();
          }
          const original = button.textContent;
          button.textContent = "已复制";
          window.setTimeout(() => {
            button.textContent = original;
          }, 1400);
        });
      });

      const navLinks = Array.from(document.querySelectorAll(".side-nav a[href^='#']"));
      const observedSections = navLinks
        .map((link) => document.querySelector(link.getAttribute("href")))
        .filter(Boolean);

      if ("IntersectionObserver" in window) {
        const observer = new IntersectionObserver((entries) => {
          const visible = entries
            .filter((entry) => entry.isIntersecting)
            .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
          if (!visible) return;
          navLinks.forEach((link) => {
            const current = link.getAttribute("href") === `#${visible.target.id}`;
            if (current) {
              link.setAttribute("aria-current", "location");
            } else {
              link.removeAttribute("aria-current");
            }
          });
        }, { rootMargin: "-20% 0px -65% 0px", threshold: [0, 0.15, 0.4] });

        observedSections.forEach((section) => observer.observe(section));
      }

      const deepLinkedArticle = location.hash
        ? document.querySelector(location.hash)
        : null;
      if (deepLinkedArticle?.classList.contains("article-unit")) {
        const details = deepLinkedArticle.querySelector("details");
        if (details) details.open = true;
      }

      updateProgress();
      updateReviewStatus();
    })();
