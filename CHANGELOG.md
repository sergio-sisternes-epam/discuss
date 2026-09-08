# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.9] - 2026-09-08

### Changed

- Resolved Atlas through marketplace `sergio-sisternes-epam` as
  `name: atlas` / `marketplace: sergio-sisternes-epam` (install identifier
  `atlas@sergio-sisternes-epam`) instead of git shorthand
  `sergio-sisternes-epam/atlas#v0.8.15`, locking catalog Atlas `v0.9.1`
  (`a1074e5`) and transitive OKF `v0.2.1` (`5246f7b`).
- Required APM CLI `0.30.0` in local setup and CI (`microsoft/apm-action`).

## [0.3.8] - 2026-09-05

### Changed

- Updated the direct Atlas dependency from `v0.8.13` to `v0.8.15`.

### Fixed

- Fetch release tag objects from the remote into an isolated
  `refs/release-tags/` namespace and run release validation against the peeled
  exact-main commit.
- Preserve `v0.3.7` as an immutable failed release attempt after its workflow
  stopped before creating a GitHub Release.

## [0.3.7] - 2026-09-04

### Added

- Added the Discuss skill for durable, agent-maintained discussion graphs,
  including speak, sprout, termination, lint, consolidation, and constellation
  paths.
- Added KVA graph rules, adversarial scenarios, and repository-owned linting.
- Added reproducible APM dependency locking, source and consumer CI, and
  exact-main release-readiness automation.

### Changed

- Migrated the discussion store from the deprecated custom mount to
  `.atlas/github.com/sergio-sisternes-epam/discuss-atlas`.
- Pinned Atlas to `v0.8.13`; Atlas owns the transitive OKF dependency.
- Updated consumer guidance to mount and resolve the private discussion store
  separately from APM package installation.

### Fixed

- Required the human-facing speak path and `speak_loaded` activation receipt.
- Clarified that the discussion store git root is the OKF root.

[Unreleased]: https://github.com/sergio-sisternes-epam/discuss/compare/v0.3.9...HEAD
[0.3.9]: https://github.com/sergio-sisternes-epam/discuss/compare/v0.3.8...v0.3.9
[0.3.8]: https://github.com/sergio-sisternes-epam/discuss/compare/v0.3.7...v0.3.8
[0.3.7]: https://github.com/sergio-sisternes-epam/discuss/tree/v0.3.7
