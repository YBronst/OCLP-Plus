# <img src="https://github.com/YBronst/OCLP-YBronst/blob/main/docs/images/OC-Patcher.png" width="48" align="center"> [OCLP-3.1.7 Tahoe Patch Set by YBronst](https://github.com/YBronst/OCLP-YBronst/releases/tag/3.1.7)

**Based on the lzhoang2801 Tahoe patchset and optimized for macOS 26.x builds.**

---

## 🌟 Key Features

### 🏔️ Full macOS Tahoe Support
Complete root patching support for **macOS Tahoe 26.0 (25A5316i)** through **macOS 26.4 (25E5233c)** and beyond. This fork ensures that legacy hardware remains compatible with the latest Darwin 25 kernel.

### 📶 Wireless & Continuity Restoration
Restores full functionality for Broadcom-based wireless chipsets (BCM4360 and similar):
*   **Wi-Fi:** Stable connectivity on 2.4GHz and 5GHz bands.
*   **AirDrop & Handoff:** Fully synchronized frameworks to ensure seamless file sharing and continuity features between devices.
*   **AirPlay:** Restored support for streaming to and from your Mac.

### 🔊 Modern Audio (AppleHDA Restoration)
Starting with macOS Tahoe Beta 2, Apple removed the legacy `AppleHDA.kext`. This patch set brings it back, ensuring built-in audio works on supported legacy systems.
*   **Manual Toggle:** A new "Modern Audio" toggle in the Root Patches menu allows you to enable or disable this restoration manually.
*   **KDK Integration:** Automatically handles the necessary Kernel Debug Kit (KDK) requirements for audio driver linking.

### 🛠️ macOS 26.4 Compatibility Fixes
*   **APFS-Only Environment:** Adapted the patching logic to handle the removal of HFS+ in macOS 26.4. The patcher now utilizes APFS for all internal resource mounting and operations.
*   **Elevated hdiutil Permissions:** Fixed a critical issue where macOS 26.4 disallowed mounting disk images without root privileges. The patcher now correctly escalates via the Privileged Helper Tool.

---

## ⚠️ Important Technical Notes

### 🔑 AMFI & Security
*   **AMFIPass Alert:** Do **NOT** use `AMFIPass.kext` with this version as it causes persistent kernel panics on Tahoe.
*   **Required Boot-Args:** You must use `amfi=0x80` to bypass Apple Mobile File Integrity checks.
*   **SIP Requirements:** Ensure System Integrity Protection is appropriately configured (typically `CSR_ALLOW_UNTRUSTED_KEXTS | CSR_ALLOW_UNRESTRICTED_FS` or `0x803`).

### 🛠️ Installation Requirements
*   **Kernel Debug Kit (KDK):** Required for most root patches on macOS 13+. Use the new **"Download KDK"** button in the Help menu to fetch the latest version.
*   **Patcher Resources:** This version relies on the [YBronst PatcherSupportPkg](https://github.com/YBronst/PatcherSupportPkg) for native Tahoe binaries.

---

## 📝 Change Log (v3.1.7)
*   Full support for Darwin 25 (macOS Tahoe).
*   Added "Modern Audio" toggle for AppleHDA restoration.
*   Fixed `hdiutil` mounting permissions for macOS 26.4.
*   Migrated internal DMG resources to APFS.
*   Improved Help menu with KDK download support.

---

## 📜 Credits

*   [Acidanthera](https://github.com/Acidanthera) (OpenCorePkg, Lilu, etc.)
*   [Dortania Team](https://github.com/dortania) (Original OCLP authors)
*   [lzhoang2801](https://github.com/kgp-macPro/OCLP-lzhoang2801) (Original Tahoe patchset)
*   [YBronst](https://github.com/YBronst) (Fork maintainer and Tahoe optimizations)
*   *Full list of OCLP contributors can be found in the [original repository](https://github.com/dortania/OpenCore-Legacy-Patcher).*

---

## ⚖️ Disclaimer
This is an **experimental fork** intended for advanced users and complex Hackintosh/Legacy Mac configurations. Use at your own risk.

**Community Discussion:** [InsanelyMac Thread](https://www.insanelymac.com/forum/topic/362042-experimental-fork-of-oclp-300-nightly-–-wi-fi-airdropairplay-and-applehda-fully-working-under-tahoe/)
