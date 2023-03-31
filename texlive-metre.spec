Name:		texlive-metre
Version:	18489
Release:	2
Summary:	Support for the work of classicists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/metre
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metre.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metre.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metre.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides classicists with some of the tools that
are needed for typesetting scholarly publications dealing with
Greek and Latin texts, with special emphasis on Greek verse. As
the package's name suggests, its core is a comprehensive set of
commands for generating metrical schemes and for placing
prosodical marks on text set in the Latin or the Greek
alphabet. The rest of the package provides a miscellany of
commands for symbols (most of them not directly related to
metre) that are often used in critical editions of classical
texts. The package does not require any special font: all
symbols are taken from the Computer Modern fonts (which are
included in all TeX distributions) and the package's commands
are based on TeX primitives.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/metre/metre.sty
%doc %{_texmfdistdir}/doc/latex/metre/README
%doc %{_texmfdistdir}/doc/latex/metre/demo.pdf
%doc %{_texmfdistdir}/doc/latex/metre/demo.tex
%doc %{_texmfdistdir}/doc/latex/metre/greek1.tex
%doc %{_texmfdistdir}/doc/latex/metre/greek2.tex
%doc %{_texmfdistdir}/doc/latex/metre/greek3.tex
%doc %{_texmfdistdir}/doc/latex/metre/igreek1.tex
%doc %{_texmfdistdir}/doc/latex/metre/igreek2.tex
%doc %{_texmfdistdir}/doc/latex/metre/igreek3.tex
%doc %{_texmfdistdir}/doc/latex/metre/metre.pdf
#- source
%doc %{_texmfdistdir}/source/latex/metre/metre.dtx
%doc %{_texmfdistdir}/source/latex/metre/metre.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
