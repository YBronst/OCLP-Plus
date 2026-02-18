# OpenCore Legacy Patcher 3.1.5 Tahoe patchset nightly
## based on OpenCore Legacy Patcher 3.0.0 Tahoe Fork.

This repository serves as a reference implementation of the last working root patching method for **macOS 26.3**. This project is a [fork of **OCLP 3.0.0 Nightly** ](https://github.com/lzhoang2801/OpenCore-Legacy-Patcher) by `lzhoang2801` (upstream commit: Dec 24, 2025).

### 🎯 Purpose & Stability
This fork specifically restores **modern Wi-Fi (AirDrop/AirPlay)** and audio (**AppleHDA**) functionality on advanced **Hackintosh** systems.
*   **Status:** Testing confirms stable and reliable performance.
*   **Compatibility:** Successfully tested on **macOS 26.3 (25D125) and below**.

### 🛠 Key Changes & Improvements (Fixed in this Fork)
1.  **Elevated Privileges: Added the necessary logic to obtain rights for mounting internal patch images and system resources.**
2.  **This fixes the mounting failures present in earlier nightly versions.**
3.  **It contains the complete `Universal-Binaries.dmg` (including AppleHDA), fixing the "missing resources" eror in the original upstream.**
6.  **Core Logic:** The fundamental root patching logic remains unchanged for maximum consistency.

### ⚠️ Compatibility Note: macOS 26.4+
Starting with **macOS 26.4 beta 1**, Apple introduced fundamental changes that render the OCLP 3.0.0 patching workflow **inoperable**, regardless of the privilege fixes included in this fork:
*   HFS-based patching workflows are no longer supported by the OS.
*   The `hdiutil` mounting method used in the 3.0.0 branch.
*   The OCLP 3.1.5 branch introduces APFS support, enabling the experimental patcher for **macOS 26.3 (25D125) and higher** bat
*   this is subject to the release of a compatible KDK required for the AppleHDA root patch.
*   **Recommendation:** For macOS 26.4 and newer, please use [OCLP-Mod 3.1.5](https://github.com/laobamac/OCLP-Mod/releases) or later, which utilizes a redesigned patching engine.

### 🔐 AMFI & Security Configuration
Distributed binaries are **unsigned**. To use them, you must:
*   Disable `AMFIPass.kext`.
*   Add boot-args: `amfi=0x80 ipc_control_port_options=0` (the latter is required for apps like Firefox to launch without AMFI).

### Important dependency
Root patching requires [PatcherSupportPkg resources provided by this preserved mirror](https://github.com/YBronst/PatcherSupportPkg).  
It contains the complete `Universal-Binaries.dmg` (including AppleHDA), fixing the "missing resources" error in the original upstream.
### 🚫 Disclaimer
This is **not an official Dortania release**. Do not use these patches on unsupported genuine Macs or systems with unsupported GPUs. Only Wi-Fi and Audio patches are expected to function.

### Credits to the Dortania OCLP team, lzhoang2801, and all PatcherSupportPkg contributors.
---
**Community Discussion:** [InsanelyMac Thread](https://www.insanelymac.com/forum/topic/362042-experimental-fork-of-oclp-300-nightly-–-wi-fi-airdropairplay-and-applehda-fully-working-under-tahoe/)
