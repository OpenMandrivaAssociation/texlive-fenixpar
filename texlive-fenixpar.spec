%global tl_name fenixpar
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.92
Release:	%{tl_revision}.1
Summary:	One-shot changes to token registers such as \everypar
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/fenixpar
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fenixpar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fenixpar.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides two packages, fenxitok and fenixpar. The fenixtok
package provides user macros to add material to a token register; the
material will be (automatically) removed from the token register when
the register is executed. Material may be added either to the left or to
the right, and care is taken not to override any redefinition that may
be included in the token register itself. The fenixpar package uses the
macros of fenixtok to provide a user interface to manipulation of the
\everypar token register. The packages require the e-TeX extensions;
with them, they work either with Plain TeX or with LaTeX.

