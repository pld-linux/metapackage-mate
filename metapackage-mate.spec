# NOTES:
# - MATE build order: http://wiki.mate-desktop.org/building#building_order
# - To see what is present in specific release, see roadmap: http://wiki.mate-desktop.org/roadmap
# - To look into future (what has less point of packaging as due being removed/deprecated):
#   http://wiki.mate-desktop.org/status:1.6
# - git page is helpful (obsolete junk under removed section): # http://git.mate-desktop.org/
# - plugins supported by community http://wiki.mate-desktop.org/plugins
#
Summary:	MATE Desktop Environment with additional packages
Summary(pl.UTF-8):	Środowisko graficzne MATE z dodatkowymi pakietami
Name:		metapackage-mate
Version:	1.5
Release:	1
License:	GPL v2+
Group:		X11/Applications
Requires:	mate-backgrounds >= %{version}
Requires:	mate-conf >= 1.4
Requires:	mate-control-center >= %{version}
Requires:	mate-desktop >= %{version}
Requires:	mate-file-manager >= %{version}
Requires:	mate-icon-theme >= %{version}
Requires:	mate-menus >= %{version}
Requires:	mate-panel >= %{version}
Requires:	mate-polkit >= %{version}
Requires:	mate-session-manager >= %{version}
Requires:	mate-settings-daemon >= %{version}
Requires:	mate-window-manager >= %{version}
Suggests:	mate-media >= %{version}
Suggests:	mate-themes >= %{version}
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
