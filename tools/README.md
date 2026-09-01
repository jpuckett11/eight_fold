# EIGHTFOLD watchers

Inherited pattern from `case_sevenfold/tools/`. Three live there and are worth
copying rather than rewriting:

| Script | Watches | Lesson it encodes |
|---|---|---|
| `watch_ca6_26-3648.py` | A federal appellate docket | CourtListener token handling, 429 backoff |
| `watch_ca10_26-4060.py` | A second docket | Only reads keywords out of an entry that actually changed. An unconditional keyword scan fires forever and trains you to ignore it |
| `watch_nd_kratom.py` | Two state bills **and** a subject sweep | A watcher keyed to specific IDs cannot see a new item appear. Sweep the whole corpus for subject terms and diff the ID set |

**Rules for any watcher added here:**

- State to `tools/.<name>.state`, changes appended to `tools/<name>_watch.log`.
  Both are gitignored so cron never dirties the tree.
- Exit 0 on no change, 10 on change. Cron entries append to `tools/cron.out`.
- **Baseline runs must not flare.** The first run writes state and says so.
- **A control that fails must report NOT USABLE, never a zero.** A timeout that
  reads as "no results found" is how a false negative enters a case file.
