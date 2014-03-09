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
Version:	1.8
Release:	1
License:	GPL v2+
Group:		X11/Applications
Requires:	caja >= %{version}
Requires:	engrampa >= %{version}
Requires:	eom >= %{version}
Requires:	gnome-keyring >= 3.0.0
Requires:	marco >= %{version}
Requires:	mate-backgrounds >= %{version}
Requires:	mate-control-center >= %{version}
Requires:	mate-desktop >= %{version}
Requires:	mate-dialogs >= %{version}
Requires:	mate-icon-theme >= %{version}
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
Requires:	atril >= %{version}
Requires:	caja-extension-atril >= %{version}
Requires:	caja-extension-engrampa >= %{version}
Requires:	caja-extension-gksu >= %{version}
Requires:	caja-extension-image-converter >= %{version}
Requires:	caja-extension-open-terminal >= %{version}
Requires:	caja-extension-sendto >= %{version}
Requires:	caja-extension-sendto-bluetooth >= %{version}
Requires:	caja-extension-sendto-burn >= %{version}
Requires:	caja-extension-sendto-emailclient >= %{version}
Requires:	caja-extension-sendto-gajim >= %{version}
Requires:	caja-extension-sendto-pidgin >= %{version}
Requires:	caja-extension-sendto-upnp >= %{version}
Requires:	caja-extension-share >= %{version}
Requires:	caja-extension-shares >= %{version}
Requires:	mate-applet-accessx-status >= %{version}
Requires:	mate-applet-battstat >= %{version}
Requires:	mate-applet-charpicker >= %{version}
Requires:	mate-applet-command >= %{version}
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
Requires:	mate-applet-timer >= %{version}
Requires:	mate-applet-trash >= %{version}
Requires:	mate-calc >= %{version}
Requires:	mate-icon-theme-faenza >= %{version}
Requires:	mate-netbook >= %{version}
Requires:	mate-system-tools >= %{version}
Requires:	mate-terminal >= %{version}
Requires:	mate-themes >= %{version}
Requires:	mate-utils >= %{version}
Requires:	mozo >= %{version}
Requires:	pluma >= %{version}

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

%files extras
%defattr(644,root,root,755)
