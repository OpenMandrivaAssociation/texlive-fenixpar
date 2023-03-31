Name:		texlive-fenixpar
Version:	24730
Release:	2
Summary:	One-shot changes to token registers such as \everypar
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/fenixpar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fenixpar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fenixpar.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides two packages, fenxitok and fenixpar. The
fenixtok package provides user macros to add material to a
token register; the material will be (automatically) removed
from the token register when the register is executed. Material
may be added either to the left or to the right, and care is
taken not to override any redefinition that may be included in
the token register itself. The fenixpar package uses the macros
of fenixtok to provide a user interface to manipulation of the
\everypar token register. The packages require the e-TeX
extensions; with them, they work either with Plain TeX or with
LaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/fenixpar/fenixpar.sty
%{_texmfdistdir}/tex/generic/fenixpar/fenixtok.sty
%doc %{_texmfdistdir}/doc/generic/fenixpar/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
