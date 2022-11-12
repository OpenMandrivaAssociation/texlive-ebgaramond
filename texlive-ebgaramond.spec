Name:		texlive-ebgaramond
Version:	64343
Release:	1
Summary:	LaTeX support for EBGaramond fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ebgaramond
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebgaramond.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebgaramond.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
EB Garamond is a revival by Georg Duffner of the 16th century
fonts designed by Claude Garamond. The LaTeX support package
works for (pdf)LaTeX, xeLaTeX and luaLaTeX users; configuration
files for use with microtype are provided.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond
%{_texmfdistdir}/fonts/map/dvips/ebgaramond
%{_texmfdistdir}/fonts/opentype/public/ebgaramond
%{_texmfdistdir}/fonts/tfm/public/ebgaramond
%{_texmfdistdir}/fonts/type1/public/ebgaramond
%{_texmfdistdir}/fonts/vf/public/ebgaramond
%{_texmfdistdir}/tex/latex/ebgaramond
%doc %{_texmfdistdir}/doc/fonts/ebgaramond

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
