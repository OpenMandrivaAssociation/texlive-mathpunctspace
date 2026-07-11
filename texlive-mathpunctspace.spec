%global tl_name mathpunctspace
%global tl_revision 46754

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Control the space after punctuation in math expressions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mathpunctspace
License:	bsd2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathpunctspace.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathpunctspace.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a mechanism to control the space after commas and
semicolons in mathematical expressions.

