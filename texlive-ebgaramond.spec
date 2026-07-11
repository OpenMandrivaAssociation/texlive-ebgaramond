%global tl_name ebgaramond
%global tl_revision 78251

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX support for EBGaramond fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ebgaramond
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ebgaramond.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ebgaramond.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(xkeyval)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
EB Garamond is a revival by Georg Duffner of the 16th century fonts
designed by Claude Garamond. The LaTeX support package works for
(pdf)LaTeX, XeLaTeX and LuaLaTeX users; configuration files for use with
microtype are provided.

