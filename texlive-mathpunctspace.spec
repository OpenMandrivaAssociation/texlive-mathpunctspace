Name:		texlive-mathpunctspace
Version:	46754
Release:	1
Summary:	Control the space after punctuation in math expressions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mathpunctspace
License:	bsd2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathpunctspace.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathpunctspace.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a mechanism to control the space after
commas and semicolons in mathematical expressions.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/mathpunctspace
%doc %{_texmfdistdir}/doc/latex/mathpunctspace

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
