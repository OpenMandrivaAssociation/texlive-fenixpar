# revision 24730
# category Package
# catalog-ctan /macros/generic/fenixpar
# catalog-date 2011-11-18 23:08:42 +0100
# catalog-license lppl
# catalog-version 0.92
Name:		texlive-fenixpar
Version:	0.92
Release:	7
Summary:	One-shot changes to token registers such as \everypar
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/fenixpar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fenixpar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fenixpar.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.92-2
+ Revision: 751830
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.92-1
+ Revision: 739749
- texlive-fenixpar

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.91-1
+ Revision: 718426
- texlive-fenixpar
- texlive-fenixpar
- texlive-fenixpar
- texlive-fenixpar

