<div align="center">
<img src="https://github.com/YBronst/OCLP-Plus/blob/main/docs/images/OC-Patcher.png"  alt="OC-Patcher Logo" width="256" />

# [OCLP-Plus (Tahoe Patch Set)](https://github.com/YBronst/OCLP-Plus/releases)

</div>

## 🌟 Key Features

### 🏔️ Full macOS Tahoe Support

* **Modern** root patching support for macOS Tahoe 26.0 (25A5316i) through macOS 26.4.1 (25E253) and later versions.
* **Supported Mac Models (SMBIOS)**: For macOS Tahoe, this patch set is designed for the following native or spoofed models:

   * **iMac**: iMac20,1, iMac20,2
   * **MacBook Pro**: MacBookPro16,1, MacBookPro16,2, MacBookPro16,4
   * **Mac Pro**: MacPro7,1

* **This set creates only $${\color{red} draft \ templates}$$** for manual configuration and does not generate ready-made EFI folders.
   * **$${\color{red}To \ avoid \ unexpected \ errors}$$, I recommend using lzhoang2801** [`OpCore Simplify`](https://github.com/lzhoang2801/OpCore-Simplify).

* **OCLP-Plus (Tahoe Patch Set)** supports macOS Sequoia 15.7.5 (24G624) and earlier, such as OpenCore Legacy Patcher 2.4.1.
* **Note**: For macOS Sequoia and earlier, compatibility and SMBIOS requirements follow the standard limits of each respective operating system.

### 📶 Wireless & Continuity
*  **Restores full functionality for Broadcom-based wireless chipsets** (BCM4360 and similar), including:

    * **AWDL support** specifically for macOS Tahoe 26.x.
    * **Stable Wi-Fi** (2.4GHz / 5GHz).
    * **AirDrop, Handoff, and AirPlay** via fully synchronized frameworks.
 
### ❌Non-functional features
*  **On majority of patched Macs, iPhone Mirroring and Apple Intelligence won't be functional.**
  
   *  iPhone Mirroring requires T2 for attestation and Apple Intelligence requires an NPU only found in Apple Silicon.
   *  The patcher is unable to provide a fix for these as they're hardware requirements.



### 🚫 Intel Wi-Fi (AirportItlwm) is NOT supported 
*  **This fork is exclusively optimized for Broadcom-based wireless chipsets.**
    *  If you require Intel Wi-Fi patches for Tahoe, please use [OCLP-Mod](https://github.com/laobamac/OCLP-Mod).

### 🔊 Modern Audio (AppleHDA Restoration)
Starting with macOS Tahoe Beta 2, Apple removed the legacy `AppleHDA.kext`. This patch set brings it back, ensuring built-in audio works on supported legacy systems.
*  **Manual Toggle:** A new "Modern Audio" toggle in the Root Patches menu allows you to enable or disable this restoration manually.
*  **KDK Integration:** Automatically handles the necessary Kernel Debug Kit (KDK) requirements for audio driver linking.

### 🛠️ macOS 26.4 Compatibility Fixes
*  **APFS-Only Environment:** Adapted the patching logic to handle the removal of HFS+ in macOS 26.4. The patcher now utilizes APFS for all internal resource mounting and operations.
>  **Elevated hdiutil Permissions:** Fixed a critical issue where macOS 26.4 disallowed mounting disk images without root privileges.
>
> The patcher now correctly escalates via the Privileged Helper Tool.

## ⚠️ Important Technical Notes
*  **Graphics patches for Deprecated accelerators in Tahoe are officially impossible. Use Sequoia for full acceleration.**

### 🔑 AMFI & Security

*  **AMFI Alert:** To successfully bypass Apple Mobile file integrity checks, you must use AMFIPass.kext with the `-amfipassbeta` boot argument.
*  **Note:** If third-party browsers (e.g., Firefox) or camera/mic permissions fail, ensure the `-amfipassbeta` boot argument is present.
*  **SIP Requirements:** System Integrity Protection must be set properly.
*  **Typical Value:** (CSR_ALLOW_UNTRUSTED_KEXTS | CSR_ALLOW_UNRESTRICTED_FS).
*  **OpenCore config.plist:** NVRAM > Add > 7C436110-AB2A-4BBB-A880-FE41995C9F82 > csr-active-config (data) <03080000>.
*  **Clover config.plist:** Set RtVariables > CsrActiveConfig (string) 0x803.
*  **Secure Boot Model:** To allow root patching for Wi-Fi and other drivers, Apple Secure Boot must be disabled.
*  **OpenCore:** Set Misc > Security > SecureBootModel to Disabled.
>
>  **Clover:** Ensure RtVariables > HWTarget is NOT set (must be empty) or commented out (e.g., HWTarget?) to keep Apple Secure Boot inactive.

### 🧹 Root Volume Dirty Error
> **If you get this error:**
>
>  **"Root volume dirty, unpatch to continue"** during the Post-Install Root Patch process, it means macOS Tahoe has flagged the system volume due to incomplete operations or APFS snapshot issues.
>
>  **To fix it:** Open OCLP-Plus on Tahoe. Go to Post-Install Root Patch and click Revert Root Patches (or Unpatch).
>  **Reboot your Mac.** Open OCLP-Plus again and **re-run the Post-Install Root Patch** normally.

### 🔄 Apply Changes: Reset NVRAM
> To ensure these new security settings (SIP, AMFI, and Secure Boot) take effect, you MUST perform a Reset NVRAM after saving your config.plist.
> OpenCore: Select "Reset NVRAM" from the boot picker menu (or press Space if it's hidden).
> Clover: Press F11 at the boot screen to clear NVRAM and restart.

### ⚒️ [`Build and run from source`](https://github.com/YBronst/OCLP-Plus/blob/main/SOURCE.md)

### 💾 Installation Requirements
💡  **Before Running Post-Install Patches:**
* **KDK is mandatory:** For macOS 13 through Tahoe (26.x), the Kernel Debug Kit must be installed for drivers like AppleHDA to link correctly. Use the Help > Download KDK button.

⚠️ **Resource Dependency Notice**
* **Patcher Resources:** This version relies on the [`PatcherSupportPkg`](https://github.com/YBronst/PatcherSupportPkg) for native Tahoe binaries.
> **Important:** Please be aware that if this resource becomes unavailable for any reason (e.g., server downtime or repository removal),
> the OCLP-3.2.1 Tahoe Patch Set will lose its ability to fetch the necessary binaries, and root patching will fail.

## 📝 [`Change Log`](https://github.com/YBronst/OCLP-Plus/blob/main/CHANGELOG.md)

## 📜 Credits
*   [`Acidanthera`](https://github.com/Acidanthera) (OpenCorePkg, Lilu, etc.)
*   [`Dortania Team`](https://github.com/dortania) (Original OCLP authors)
*   [`lzhoang2801`](https://github.com/kgp-macPro/OCLP-lzhoang2801) (Original Tahoe patchset)
*   [`CloverHackyColor`](https://github.com/CloverHackyColor) (Hackintosh essentials and beyond)
*   [`YBronst`](https://github.com/YBronst) (Developer and optimizer of tools for macOS Tahoe26.x)
*   [`laobamac`](https://github.com/laobamac) (Developer OCLP-Mod, Chinese language)
*   *Full list of OCLP contributors can be found in the [`original repository`](https://github.com/dortania/OpenCore-Legacy-Patcher).*

## ⚖️ Disclaimer
This is an **experimental Project** intended for advanced users and complex Hackintosh/Legacy Mac configurations. Use at your own risk.

**Community Discussion:** [`InsanelyMac Thread`](https://www.insanelymac.com/forum/topic/362543-the-latest-the-oclp-plus-321-tahoe-patch-set-is-out/)
