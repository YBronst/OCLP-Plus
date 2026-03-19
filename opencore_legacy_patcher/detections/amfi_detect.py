"""
amfi_detect.py: Determine AppleMobileFileIntegrity's OS configuration
"""

import enum
import subprocess
import os

class AmfiConfigDetectLevel(enum.IntEnum):
    """
    Configuration levels used by AmfiConfigurationDetection
    """

    NO_CHECK:                   int = 0
    LIBRARY_VALIDATION:         int = 1  # For Ventura, use LIBRARY_VALIDATION_AND_SIG
    LIBRARY_VALIDATION_AND_SIG: int = 2
    ALLOW_ALL:                  int = 3


class AmfiConfigurationDetection:
    """
    Detect AppleMobileFileIntegrity's OS configuration

    Usage:

    >>> import amfi_detect
    >>> can_patch = amfi_detect.AmfiConfigurationDetection().check_config(amfi_detect.AmfiConfigDetectLevel.ALLOW_ALL)

    """

    def __init__(self, xnu_major: int = None) -> None:
        self.SKIP_LIBRARY_VALIDATION: bool = False
        self.SIP_SUITABLE:            bool = False

        if xnu_major:
            self._xnu_major = xnu_major
        else:
            self._xnu_major = int(os.uname().release.split(".")[0])

        self._detect_live_kernel_state()
        self._check_sip_status()


    def _detect_live_kernel_state(self) -> None:
        """
        Detect live kernel state for AMFI
        Specifically, check if Library Validation is disabled
        """
        try:
            result = subprocess.run(["sysctl", "-n", "vm.cs_library_validation"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if result.returncode == 0:
                if result.stdout.decode().strip() == "0":
                    self.SKIP_LIBRARY_VALIDATION = True
        except:
            pass


    def _check_sip_status(self) -> None:
        """
        Check SIP status via csrutil
        """
        try:
            result = subprocess.run(["/usr/bin/csrutil", "status"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if result.returncode == 0:
                output = result.stdout.decode()
                if "System Integrity Protection status: disabled." in output:
                    self.SIP_SUITABLE = True
                elif "System Integrity Protection status: unknown (Custom Configuration)." in output:
                    # Check for Filesystem Protections and Kext Signing
                    if "Filesystem Protections: disabled" in output and "Kext Signing: disabled" in output:
                        self.SIP_SUITABLE = True
        except:
            pass


    def check_config(self, level: int) -> bool:
        """
        Check the AMFI configuration based on provided AMFI level
        See AmfiConfigLevel enum for valid levels

        Parameters:
            level (int): The level of AMFI checks to check for

        Returns:
            bool: True if the AMFI configuration matches the level, False otherwise
        """

        if level == AmfiConfigDetectLevel.NO_CHECK:
            return True

        # For macOS below 11.0 (Big Sur), only SIP status matters
        if self._xnu_major < 20:
            return self.SIP_SUITABLE

        # For macOS 11.0 and above, both SIP and Live AMFI Status (Library Validation) matter
        return bool(self.SIP_SUITABLE and self.SKIP_LIBRARY_VALIDATION)
