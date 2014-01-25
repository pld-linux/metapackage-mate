# NOTES:
# - MATE build order: http://wiki.mate-desktop.org/building#building_order
# - To see what is present in specific release, see roadmap: http://wiki.mate-desktop.org/roadmap
# - To look into future (what has less point of packaging as due being removed/deprecated):
#   http://wiki.mate-desktop.org/status:1.6
# - git page is helpful (obsolete junk under removed section): # http://git.mate-desktop.org/
# - plugins supported by community http://wiki.mate-desktop.org/plugins
# - OpenSUSE MATE page: http://en.opensuse.org/MATE_Desktop
#
Summary:	MATE Desktop Environment - core packages
Summary(pl.UTF-8):	Środowisko graficzne MATE - pakiety podstawowe
Name:		metapackage-mate
Version:	1.6
Release:	2
License:	GPL v2+
Group:		X11/Applications
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
Suggests:	%{name}-extras = %{version}-%{release}
Suggests:	pulseaudio-alsa
Suggests:	xscreensaver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MATE Desktop Environment (metapackage). This brings core MATE
packages.

MATE is a fork of GNOME 2. It provides an intuitive and attractive
desktop to Linux users using traditional metaphors.

%description -l pl.UTF-8
Środowisko graficzne MATE (metapakiet). Ten metapakiet obejmuje
podstawowe pakiety MATE.

MATE to odgałęzienie GNOME 2. Zapewnia intuicyjne i atrakcyjne
środowisko graficzne dla użytkowników Linuksa przy użyciu tradycyjnych
metafor.

%package extras
Summary:	MATE Desktop Environment - additional packages
Summary(pl.UTF-8):	Środowisko graficzne MATE - pakiety opcjonalne
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	mate-applet-accessx-status >= %{version}
Requires:	mate-applet-battstat >= %{version}
Requires:	mate-applet-charpicker >= %{version}
Requires:	mate-applet-cpufreq >= %{version}
Requires:	mate-applet-drivemount >= %{version}
Requires:	mate-applet-geyes >= %{version}
Requires:	mate-applet-gweather >= %{version}
Requires:	mate-applet-indicator >= %{version}
Requires:	mate-applet-invest >= %{version}
Requires:	mate-applet-multiload >= %{version}
Requires:	mate-applet-netspeed >= %{version}
Requires:	mate-applet-sensors >= %{version}
Requires:	mate-applet-stickynotes >= %{version}
Requires:	mate-applet-trash >= %{version}
Requires:	mate-bluetooth >= %{version}
Requires:	mate-calc >= %{version}
Requires:	mate-character-map >= %{version}
Requires:	mate-document-viewer >= %{version}
Requires:	mate-file-manager-extension-atril >= %{version}
Requires:	mate-file-manager-extension-engrampa >= %{version}
Requires:	mate-file-manager-extension-gksu >= %{version}
Requires:	mate-file-manager-extension-image-converter >= %{version}
Requires:	mate-file-manager-extension-open-terminal >= %{version}
Requires:	mate-file-manager-extension-share >= %{version}
Requires:	mate-file-manager-extension-shares >= %{version}
Requires:	mate-file-manager-sento >= %{version}
Requires:	mate-file-manager-sento-bluetooth >= %{version}
Requires:	mate-file-manager-sento-burn >= %{version}
Requires:	mate-file-manager-sento-emailclient >= %{version}
Requires:	mate-file-manager-sento-gajim >= %{version}
Requires:	mate-file-manager-sento-pidgin >= %{version}
Requires:	mate-file-manager-sento-upnp >= %{version}
Requires:	mate-icon-theme-faenza >= %{version}
Requires:	mate-menu-editor >= %{version}
Requires:	mate-netbook >= %{version}
Requires:	mate-system-tools >= %{version}
Requires:	mate-terminal >= %{version}
Requires:	mate-text-editor >= %{version}
Requires:	mate-themes >= %{version}
Requires:	mate-user-share >= %{version}
Requires:	mate-utils >= %{version}

%description extras
MATE Desktop Environment (metapackage). This brings additional MATE
packages.

%description extras -l pl.UTF-8
Środowisko graficzne MATE (metapakiet). Ten metapakiet obejmuje
dodatkowe, opcjonalne pakiety MATE.

%prep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
