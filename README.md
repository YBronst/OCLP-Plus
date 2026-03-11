# [OCLP-3.1.7 Tahoe Patch Set by YBronst](https://github.com/YBronst/OCLP-YBronst/releases/edit/3.1.7)
**Based on the lzhoang2801 Tahoe patchset (Dec 24, 2025 state).**

## OCLP-YBronst 3.1.7 - Tahoe Patch Set

### ⚠️ Attention
* **AMFIPass** cannot be used with OCLP 3.1.7 due to a persistent kernel panic. Instead, use the `amfi=0x80` boot argument.

### 📝 Change log
* **Dynamic Fallback Mechanism:** When running on macOS Tahoe (XNU 25), the root patching engine now automatically attempts to use resources with the `-24` suffix (Sequoia) if the `-25` directory is missing. 
* **Compatibility:** Full support for **macOS Tahoe 26.0 (25A5316i)** through **macOS 26.4 (25E5233c)**, with potential support for subsequent 26.x builds.
* **HFS+ Removal Adaptation:** Apple removed the HFS+ file system in macOS 26.4. This version adapts the patching logic to remain compatible with the now APFS-only system environment.
* **hdiutil Permissions:** Fixed an issue where macOS 26.4 disallowed mounting via `hdiutil` without root privileges.
* **Modern Audio Toggle:** Added a toggle to the **Root Patches** menu to enable/disable the 'Modern Audio' patch (AppleHDA restoration). This provides manual control and prevents panics if a matching KDK is not yet installed for future builds.
* **KDK Support:** A new button in the Help menu allows downloading the latest Kernel Debug Kit.

For systems requiring a fully functional reference environment (including sound) on macOS 26.3 and earlier, I recommend a saved and working patch snapshot from December 24th, available here: [`OCLP-lzhoang2801`](https://github.com/kgp-macPro/OCLP-lzhoang2801)

*Note: This patch set still requires the `amfi=0x80` boot argument.*

---
## Credits

* [Acidanthera](https://github.com/Acidanthera)
  * OpenCorePkg, as well as many of the core kexts and tools
* [DhinakG](https://github.com/DhinakG)
  * Main co-author
* [Khronokernel](https://github.com/Khronokernel)
  * Main co-author
* [Ausdauersportler](https://github.com/Ausdauersportler)
  * iMacs Metal GPUs Upgrade Patch set and documentation
  * Great amounts of help with debugging, and code suggestions
* [vit9696](https://github.com/vit9696)
  * Endless amount of help troubleshooting, determining fixes and writing patches
* [EduCovas](https://github.com/covasedu)
  * [non-Metal patch set](https://github.com/moraea/non-metal-frameworks) for nVidia Tesla/Fermi/Maxwell/Pascal, AMD TeraScale 1/2, and Intel Core 1st/2nd Generation GPUs
  * [3802 Metal patch set](https://github.com/moraea/misc-patches/tree/main/3802-Metal-15) and [MetallibSupportPkg](https://github.com/dortania/MetallibSupportPkg) for nVidia Kepler and Intel Core 3rd/4th Generation GPUs
  * Metal bundle patches and shims for [nVidia Kepler](https://github.com/moraea/misc-patches/tree/main/Kepler%2013%2B), [AMD GCN 1 - 4](https://github.com/moraea/misc-patches/tree/main/GCN%2013%2B), and [AMD GCN 5 (Vega)](https://github.com/moraea/misc-patches/tree/main/vega%2013%2B)
  * [IOSurface offset patches](https://github.com/moraea/misc-patches/tree/main/Sonoma%2014.4%20IOSurface) for nVidia Kepler, AMD GCN 1 - 5, and Intel Core 3rd - 6th Generation GPUs
  * [legacy Wi-Fi patch set](https://github.com/moraea/unsupported-wifi-patches) restores functionality for Wi-Fi cards in all 2007 - 2017 models
  * [T1 patch set](https://github.com/moraea/misc-patches/tree/main/T1-Patch) restores Touch ID, Apple Pay, and other secure functionality in 2016 - 2017 models
  * AppleGVA downgrade for accelerated video decoding on 2012 - 2016 models
  * OpenCL and OpenGL downgrade for AMD GCN
  * [USB 1 patch](https://github.com/moraea/misc-patches/tree/main/IOUSBHostFamily-14.4)
* [ASentientHedgehog](https://github.com/moosethegoose2213)
  * [non-Metal patch set](https://github.com/moraea/non-metal-frameworks) for nVidia Tesla/Fermi/Maxwell/Pascal, AMD TeraScale 1/2, and Intel Core 1st/2nd Generation GPUs
* [ASentientBot](https://github.com/ASentientBot)
  * [non-Metal patch set](https://github.com/moraea/non-metal-frameworks) for nVidia Tesla/Fermi/Maxwell/Pascal, AMD TeraScale 1/2, and Intel Core 1st/2nd Generation GPUs
  * [Metal bundle interposer](https://github.com/moraea/misc-patches/tree/main/sequoia%2031001%20interposer) for AMD GCN 1 - 5 and Intel Core 5th/6th Generation GPUs
  * [dsce](https://github.com/moraea/dsce) and [shared code](https://github.com/moraea/moraea-common) used by some other patches
* [cdf](https://github.com/cdf)
  * Mac Pro on OpenCore Patch set and documentation
  * [Innie](https://github.com/cdf/Innie) and [NightShiftEnabler](https://github.com/cdf/NightShiftEnabler)
* [Syncretic](https://forums.macrumors.com/members/syncretic.1173816/)
  * [AAAMouSSE](https://forums.macrumors.com/threads/mp3-1-others-sse-4-2-emulation-to-enable-amd-metal-driver.2206682/), [telemetrap](https://forums.macrumors.com/threads/mp3-1-others-sse-4-2-emulation-to-enable-amd-metal-driver.2206682/post-28447707) and [SurPlus](https://github.com/reenigneorcim/SurPlus)
* [dosdude1](https://github.com/dosdude1)
  * Main author of the [original GUI](https://github.com/dortania/OCLP-GUI)
  * Development of previous patchers, laying out much of what needs to be patched
* [parrotgeek1](https://github.com/parrotgeek1)
  * [VMM Patch Set](https://github.com/dortania/OpenCore-Legacy-Patcher/blob/4a8f61a01da72b38a4b2250386cc4b497a31a839/payloads/Config/config.plist#L1222-L1281)
* [BarryKN](https://github.com/BarryKN)
  * Development of previous patchers, laying out much of what needs to be patched
* [mario_bros_tech](https://github.com/mariobrostech) and the rest of the Unsupported Mac Discord
  * Catalyst that started OCLP-YBronst 3.1.6
* [arter97](https://github.com/arter97/)
  * [SimpleMSR](https://github.com/arter97/SimpleMSR/) to disable firmware throttling in Nehalem+ MacBooks without batteries
* [Mr.Macintosh](https://mrmacintosh.com)
  * Endless hours helping architect and troubleshoot many portions of the project
* [flagers](https://github.com/flagersgit)
  * Aid with Nvidia Web Driver research and development
  * [non-Metal patch set](https://github.com/moraea/non-metal-frameworks) for nVidia Tesla/Fermi/Maxwell/Pascal, AMD TeraScale 1/2, and Intel Core 1st/2nd Generation GPUs
  * [Metal bundle interposer](https://github.com/moraea/misc-patches/tree/main/sequoia%2031001%20interposer) for AMD GCN 1 - 5 and Intel Core 5th/6th Generation GPUs
  * LegacyRVPL, SnapshotIsKill, etc. to aid in rapid testing and development
* [joevt](https://github.com/joevt)
  * [FixPCIeLinkrate](https://github.com/joevt/joevtApps)
* [Jazzzny](https://github.com/Jazzzny)
  * Research and various contributions to the project
  * UEFI Legacy XHCI research and development
  * NVIDIA OpenCL research and development
  * `MacBook5,2` research and development
    * LegacyKeyboardInjector
  * Pre-Ivy Bridge Aquantia Ethernet Patch
  * Non-Metal Photo Booth Patch for Monterey+
  * GUI and Backend Development
    * Updater UI
    * macOS Downloader UI
    * Downloader UI
    * USB Top Case probing
    * Developer root patching
  * Vaulting implementation
  * macOS 15 3802 Helios Research
  * UEFI bootx64.efi research
  * universal2 build research
  * Various documentation contributions
* Amazing users who've graciously donate hardware:
  * [JohnD](https://forums.macrumors.com/members/johnd.53633/) - 2013 Mac Pro
  * [SpiGAndromeda](https://github.com/SpiGAndromeda) - AMD Vega 64
  * [turbomacs](https://github.com/turbomacs) - 2014 5k iMac
  * [vinaypundith](https://forums.macrumors.com/members/vinaypundith.1212357/) - MacBook7,1
   * [ThatStella7922](https://github.com/ThatStella7922) - 2017 13" MacBook Pro (A1708)
  * zephar - 2008 Mac Pro
  * jazo97 - 2011 15" MacBook Pro
  * And others (reach out if we forgot you!)
* MacRumors and Unsupported Mac Communities
  * Endless testing and reporting issues
* Apple
  * for macOS and many of the kexts, frameworks and other binaries we reimplemented into newer OSes

## Disclaimer
This is **not an official Dortania release** and is intended for complex Hackintosh configurations.

**Thanks to:**
* Dortania OCLP team
* lzhoang2801
* All PatcherSupportPkg contributors



**Community discussion:** [InsanelyMac thread](https://www.insanelymac.com/forum/topic/362042-experimental-fork-of-oclp-300-nightly-–-wi-fi-airdropairplay-and-applehda-fully-working-under-tahoe/)

