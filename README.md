<div align="center">
<img src="https://github.com/YBronst/OCLP-Plus/blob/main/docs/images/OC-Patcher.png"  alt="OC-Patcher Logo" width="256" />

# [OCLP-Plus (Tahoe Patch Set)](https://github.com/YBronst/OCLP-Plus/releases)

</div>

## 🌟 Key Features

### 🏔️ Full macOS Tahoe Support
Complete root patching support for **macOS Tahoe 26.0 (25A5316i)** through **macOS 26.4 (25E5233c)** and beyond. This fork ensures that legacy hardware remains compatible with the latest Darwin 25 kernel.

### 📶 Wireless & Continuity Restoration
Restores full functionality for Broadcom-based wireless chipsets (BCM4360 and similar):
*  **Wi-Fi:** Stable connectivity on 2.4GHz and 5GHz bands.
*  **AirDrop & Handoff:** Fully synchronized frameworks to ensure seamless file sharing and continuity features between devices.
*  **AirPlay:** Restored support for streaming to and from your Mac.

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

*  **AMFI Alert:** To successfully bypass Apple Mobile file integrity checks, you must use either AMFIPass.kext with the `-amfipassbeta` boot argument or `amfi=0x80`. You can also use both together.
*  **Note:**  If third-party browsers (e.g., Firefox) or camera/mic permissions fail while using `amfi=0x80`, try adding the `ipc_control_port_options=0` parameter to your boot arguments.
*  **SIP Requirements:** System Integrity Protection must be set properly.
*  **Typical Value:** (CSR_ALLOW_UNTRUSTED_KEXTS | CSR_ALLOW_UNRESTRICTED_FS).
*  **OpenCore config.plist:** NVRAM > Add > 7C436110-AB2A-4BBB-A880-FE41995C9F82 > csr-active-config (data) <03080000>.
*  **Clover config.plist:** Set RtVariables > CsrActiveConfig (string) 0x803.
*  **Secure Boot Model:** To allow root patching for Wi-Fi and other drivers, Apple Secure Boot must be disabled.
*  **OpenCore:** Set Misc > Security > SecureBootModel to Disabled.
>
>  **Clover:** Ensure RtVariables > HWTarget is NOT set (must be empty) or commented out (e.g., HWTarget?) to keep Apple Secure Boot inactive.

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
> the OCLP-3.1.9 Tahoe Patch Set will lose its ability to fetch the necessary binaries, and root patching will fail.

## 📝 [`Change Log`](https://github.com/YBronst/OCLP-Plus/blob/main/CHANGELOG.md)

## 📜 Credits
*   [`Acidanthera`](https://github.com/Acidanthera) (OpenCorePkg, Lilu, etc.)
*   [`Dortania Team`](https://github.com/dortania) (Original OCLP authors)
*   [`lzhoang2801`](https://github.com/kgp-macPro/OCLP-lzhoang2801) (Original Tahoe patchset)
*   [`CloverHackyColor`](https://github.com/CloverHackyColor) (Hackintosh essentials and beyond)
*   [`YBronst`](https://github.com/YBronst) (Developer and optimizer of tools for macOS Tahoe26.x)
*   *Full list of OCLP contributors can be found in the [`original repository`](https://github.com/dortania/OpenCore-Legacy-Patcher).*

## ⚖️ Disclaimer
This is an **experimental Project** intended for advanced users and complex Hackintosh/Legacy Mac configurations. Use at your own risk.

**Community Discussion:** [`InsanelyMac Thread`](https://www.insanelymac.com/forum/topic/362543-the-latest-the-oclp-plus-318-tahoe-patch-set-is-out/)
