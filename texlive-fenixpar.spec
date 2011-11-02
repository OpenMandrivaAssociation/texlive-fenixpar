Name:		texlive-fenixpar
Version:	0.91
Release:	1
Summary:	One-shot changes to token registers such as \everypar
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/fenixpar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fenixpar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fenixpar.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/fenixpar/fenixpar.sty
%{_texmfdistdir}/tex/generic/fenixpar/fenixtok.sty
%doc %{_texmfdistdir}/doc/generic/fenixpar/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
