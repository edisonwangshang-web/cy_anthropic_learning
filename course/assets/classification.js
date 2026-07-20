    (() => {
      const search = document.getElementById("articleSearch");
      const articles = Array.from(document.querySelectorAll(".article"));
      const filterButtons = Array.from(document.querySelectorAll("[data-filter]"));
      const resultCount = document.getElementById("resultCount");
      const emptyState = document.getElementById("emptyState");
      let activeFilter = "all";

      const normalize = (value) => value.toLocaleLowerCase().trim();

      const applyFilters = () => {
        const query = normalize(search.value);
        let visibleCount = 0;

        articles.forEach((article) => {
          const matchesCategory = activeFilter === "all" || article.dataset.category === activeFilter;
          const searchable = normalize(`${article.dataset.search} ${article.textContent}`);
          const matchesSearch = !query || searchable.includes(query);
          const visible = matchesCategory && matchesSearch;
          article.hidden = !visible;
          if (visible) visibleCount += 1;
        });

        resultCount.textContent = `显示 ${visibleCount} 篇文章`;
        emptyState.classList.toggle("is-visible", visibleCount === 0);
      };

      search.addEventListener("input", applyFilters);

      filterButtons.forEach((button) => {
        button.addEventListener("click", () => {
          activeFilter = button.dataset.filter;
          filterButtons.forEach((item) => {
            item.setAttribute("aria-pressed", String(item === button));
          });
          applyFilters();
        });
      });

      applyFilters();
    })();
