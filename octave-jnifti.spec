%global octpkg jnifti

Summary:	A fast NIfTI-1/2 reader and NIfTI-to-JNIfTI converter for Octave
Name:		octave-%{octpkg}
Version:	0.6
Release:	1
Source0:	https://github.com/fangq/%{octpkg}/archive/v%{version}/%{octpkg}-%{version}.tar.gz
License:	Apache and BDS and GPLv3+
Group:		Sciences/Mathematics
Url:		https://github.com/fangq/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 4.0.0
#BuildRequires:	octave-jsonlab
#BuildRequires:	octave-zmat

Requires:	octave(api) = %{octave_api}
Requires:	octave-jsonlab
Requires:	octave-zmat

Requires(post): octave
Requires(postun): octave

%description
The JNIfTI toolbox provides add NIfTI-1/2 read/write supports to GNU Octave.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

# fix path
mkdir inst
mkdir src
mv lib/matlab/*.m inst
mv lib/octave/*.m inst
mv lib/matlab/LICENSE_GPLv3.txt COPYING
sed -i -e 's/^%!.*$//g' inst/niftiread.m inst/niftiwrite.m inst/niftiinfo.m

# add missind description (from debian)
cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: 2020-15-06
Title: fast NIfTI-1/2 reader and NIfTI-to-JNIfTI converter for Octave
Author: Qianqian Fang <fangqq@gmail.com>
Maintainer: Qianqian Fang <fangqq@gmail.com>
Description: JNIfTI Toolbox is a fully functional NIfTI-1/2 reader/writer that supports both
 MATLAB and GNU Octave, and is capable of reading/writing both non-compressed
 and compressed NIfTI files (.nii, .nii.gz) as well as two-part Analyze7.5/NIfTI
 files (.hdr/.img and .hdr.gz/.img.gz). 
 More importantly, this is a toolbox that converts NIfTI data to its JSON-based
 replacement, JNIfTI (.jnii for text-based and .bnii for binary-based), defined
 by the JNIfTI specification (http://github.com/fangq/jnifti). JNIfTI is a
 much more flexible, human-readable and extensible file format compared to the
 more rigid and opaque NIfTI format, making the data much easier to manipulate
 and share.
URL: https://github.com/fangq/jnifti
Depends: jsonlab, zmat
Categories: JNIfTI
EOF

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

