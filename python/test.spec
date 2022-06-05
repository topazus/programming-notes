%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname alacritty

Name:           %{appname}-git
Version:        3.11.0a7
Release:        1%{?dist}
Summary:        Fast, cross-platform, OpenGL terminal emulator

License:        ASL 2.0 or MIT
URL:            https://github.com/alacritty/alacritty
Source:         https://github.com/alacritty/alacritty/archive/master/alacritty-master.tar.>
