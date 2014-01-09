# NOTES:
# - MATE build order: http://wiki.mate-desktop.org/building#building_order
# - To see what is present in specific release, see roadmap: http://wiki.mate-desktop.org/roadmap
# - To look into future (what has less point of packaging as due being removed/deprecated):
#   http://wiki.mate-desktop.org/status:1.6
# - git page is helpful (obsolete junk under removed section): # http://git.mate-desktop.org/
# - plugins supported by community http://wiki.mate-desktop.org/plugins
# - OpenSUSE MATE page: http://en.opensuse.org/MATE_Desktop
#
Summary:	MATE Desktop Environment with additional packages
Summary(pl.UTF-8):	Środowisko graficzne MATE z dodatkowymi pakietami
Name:		metapackage-mate
Version:	1.6
Release:	1
License:	GPL v2+
Group:		X11/Applications
# core packages
Requires:	mate-backgrounds >= %{version}
Requires:	mate-control-center >= %{version}
Requires:	mate-desktop >= %{version}
Requires:	mate-dialogs >= %{version}
Requires:	mate-file-archiver >= %{version}
Requires:	mate-file-manager >= %{version}
Requires:	mate-icon-theme >= %{version}
Requires:	mate-image-viewer >= %{version}
Requires:	mate-keyring >= %{version}
Requires:	mate-media >= %{version}
Requires:	mate-menus >= %{version}
Requires:	mate-notification-daemon >= %{version}
Requires:	mate-panel >= %{version}
Requires:	mate-polkit >= %{version}
Requires:	mate-power-manager >= %{version}
Requires:	mate-screensaver >= %{version}
Requires:	mate-session-manager >= %{version}
Requires:	mate-settings-daemon >= %{version}
Requires:	mate-system-monitor >= %{version}
Requires:	mate-window-manager >= %{version}
# extras
Suggests:	mate-applet-accessx-status >= %{version}
Suggests:	mate-applet-battstat >= %{version}
Suggests:	mate-applet-charpicker >= %{version}
Suggests:	mate-applet-cpufreq >= %{version}
Suggests:	mate-applet-drivemount >= %{version}
Suggests:	mate-applet-geyes >= %{version}
Suggests:	mate-applet-gweather >= %{version}
Suggests:	mate-applet-indicator >= %{version}
Suggests:	mate-applet-invest >= %{version}
Suggests:	mate-applet-multiload >= %{version}
Suggests:	mate-applet-netspeed >= %{version}
Suggests:	mate-applet-sensors >= %{version}
Suggests:	mate-applet-stickynotes >= %{version}
Suggests:	mate-applet-trash >= %{version}
Suggests:	mate-bluetooth >= %{version}
Suggests:	mate-calc >= %{version}
Suggests:	mate-character-map >= %{version}
Suggests:	mate-document-viewer >= %{version}
Suggests:	mate-file-manager-extension-atril >= %{version}
Suggests:	mate-file-manager-extension-engrampa >= %{version}
Suggests:	mate-file-manager-extension-gksu >= %{version}
Suggests:	mate-file-manager-extension-image-converter >= %{version}
Suggests:	mate-file-manager-extension-open-terminal >= %{version}
Suggests:	mate-file-manager-extension-share >= %{version}
Suggests:	mate-file-manager-extension-shares >= %{version}
Suggests:	mate-file-manager-sento >= %{version}
Suggests:	mate-file-manager-sento-bluetooth >= %{version}
Suggests:	mate-file-manager-sento-burn >= %{version}
Suggests:	mate-file-manager-sento-emailclient >= %{version}
Suggests:	mate-file-manager-sento-gajim >= %{version}
Suggests:	mate-file-manager-sento-pidgin >= %{version}
Suggests:	mate-file-manager-sento-upnp >= %{version}
Suggests:	mate-icon-theme-faenza >= %{version}
Suggests:	mate-menu-editor >= %{version}
Suggests:	mate-netbook >= %{version}
Suggests:	mate-system-tools >= %{version}
Suggests:	mate-terminal >= %{version}
Suggests:	mate-text-editor >= %{version}
Suggests:	mate-themes >= %{version}
Suggests:	mate-user-share >= %{version}
Suggests:	mate-utils >= %{version}
Suggests:	pulseaudio-alsa
Suggests:	xscreensaver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MATE Desktop Environment with additional packages (metapackage).

MATE is a fork of GNOME 2. It provides an intuitive and attractive
desktop to Linux users using traditional metaphors.

%description -l pl.UTF-8
Środowisko graficzne MATE z dodatkowymi pakietami (metapakiet).

MATE to odgałęzienie GNOME 2. Zapewnia intuicyjne i atrakcyjne
środowisko graficzne dla użytkowników Linuksa przy użyciu tradycyjnych
metafor.

%prep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
