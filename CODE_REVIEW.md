# Code Review for OCLP-Plus (Tahoe Patch Set)

## Overview
This review focuses on the changes introduced in the YBronst fork to support macOS Tahoe (Darwin 25) and address issues in recent 26.x builds.

## Findings

### 1. Modern Wireless & AirDrop Support (`modern_wireless.py`)
- **Observation:** In `_extended_patch()`, there is a guard: `if self._xnu_major > os_data.sonoma: return {}`.
- **Impact:** This means that for macOS Sequoia (XNU 24) and macOS Tahoe (XNU 25), the "Modern Wireless Extended" patches (which include `CoreWiFi.framework` and `CoreWLAN.framework` synchronization) are **skipped**.
- **Discrepancy Note:** Memory records suggest this gate was intended to be removed and `CoreWLAN.framework` moved to `PrivateFrameworks` for Tahoe. However, the current code still contains the gate and uses the standard `Frameworks` path for Sonoma only.
- **Recommendation:** If AirDrop/Handoff functionality is desired on Tahoe, this guard should be removed or updated to include `os_data.tahoe`, and `CoreWLAN.framework` should likely be moved to `PrivateFrameworks` as per the intended design for Darwin 25.

### 2. Modern Audio (AppleHDA Restoration) (`modern_audio.py`)
- **Observation:** The implementation correctly targets Darwin 25 and excludes Tahoe Beta 1 (build `25A5279m`) where AppleHDA was still present.
- **Good Practice:** The use of `requires_kernel_debug_kit() = True` is correct as these kexts now require KDK for proper linking in newer macOS versions.
- **Recommendation:** Ensure that the `allow_modern_audio` toggle in `Constants` is easily accessible in the GUI (already implemented in `gui_settings.py`).

### 3. Privilege Escalation for `hdiutil` (`dmg_mount.py`)
- **Observation:** The method `_mount_universal_binaries_dmg` now uses `subprocess_wrapper.run_as_root` for the `hdiutil attach` command.
- **Impact:** This successfully addresses the mounting permission issues introduced in macOS 26.4.
- **Recommendation:** Verify that the Privileged Helper Tool is correctly installed and signed, as `run_as_root` depends on it.

### 4. HFS+ to APFS Transition (`ci_tooling/build_modules/disk_images.py`)
- **Observation:** The `payloads.dmg` generation now explicitly uses `-fs APFS`.
- **Impact:** Ensures compatibility with macOS 26.4 and newer where HFS+ support was removed (and then partially returned, but APFS remains the safer default for system resources).

### 5. OS Data and Constants (`os_data.py`, `constants.py`)
- **Observation:** `tahoe` is correctly mapped to XNU version 25.
- **Observation:** Constants point to the YBronst fork for updates and resources.

## Suggested Improvements
1. **AirDrop on Tahoe:** Re-evaluate the `_xnu_major > os_data.sonoma` check in `modern_wireless.py`. If the frameworks from 13.7.2 are still compatible with Tahoe's private frameworks, they should be enabled to restore full AirDrop functionality.
2. **Localization:** While the primary language is English, ensure that new strings (like the Modern Audio toggle) are added to the translation files to avoid "Missing String" errors in the GUI for other locales.
3. **AMFI Documentation:** Use `-amfipassbeta` for AMFI bypass with AMFIPass.kext.

## Conclusion
The fork successfully implements the necessary "stop-gap" measures for Tahoe support. The most significant achievement is the restoration of AppleHDA and the fix for `hdiutil` permissions. Addressing the AirDrop patch logic for XNU 25 would be the next logical step for feature parity.
