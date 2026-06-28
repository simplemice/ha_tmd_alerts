# Changelog

## [2.2.5] - 2026-06-28

### Fixed
- use first API field for English text and add auto language detection

---

## [2.2.4] - 2026-06-28

### Fixed
- move brand assets to correct location and add icon.png

---

## [2.2.3] - 2026-06-28

### Fixed
- show None instead of empty state when no active warnings

---

## [2.2.2] - 2026-06-28

### Other
- fix workflow
- add brand logo & screenshot
- add more screenshot and fix README.md
- fix CHANGELOG.md

---

## [2.2.1] - 2026-06-28

### Fixed
- reload coordinator on language change, fix OptionsFlow for HA 2024.11+ (v2.2.1)

- Add update_listener in async_setup_entry so language change via Configure
  reloads the integration immediately without manual HA restart

- Remove config_entry argument from TMDOptionsFlow.__init__ (deprecated in
  HA 2024.11+, caused Configure button to silently fail)

- Bump to v2.2.1

### Other
- fix CHANGELOG.md

---

## [2.2.0] - 2026-06-27

### Added
- add bilingual support (EN/TH) selectable at install and via options (v2.2.0)

- Add CONF_LANGUAGE, LANG_EN, LANG_TH constants

- Config flow shows English / ภาษาไทย selector at install time

- OptionsFlow allows language change post-install via Configure button

- API returns both _en and _th fields for all text fields

- Sensors use coordinator.language to pick correct language field

- _last_text() fix for TMD API duplicate-element bug (first English field contains Thai)

- Translations updated with language field and options flow section

- Add CHANGELOG.md 

### Other
- add screenshot
