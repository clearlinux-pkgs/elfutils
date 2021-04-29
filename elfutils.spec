#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFC57E3CCACD99A78 (mjw@gnu.org)
#
%define keepstatic 1
Name     : elfutils
Version  : 0.183
Release  : 76
URL      : https://sourceware.org/elfutils/ftp/0.183/elfutils-0.183.tar.bz2
Source0  : https://sourceware.org/elfutils/ftp/0.183/elfutils-0.183.tar.bz2
Source1  : https://sourceware.org/elfutils/ftp/0.183/elfutils-0.183.tar.bz2.sig
Summary  : A collection of utilities and DSOs to handle ELF files and DWARF data
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-2.0+ GPL-3.0 GPL-3.0+ LGPL-3.0 LGPL-3.0+
Requires: elfutils-bin = %{version}-%{release}
Requires: elfutils-lib = %{version}-%{release}
Requires: elfutils-license = %{version}-%{release}
Requires: elfutils-locales = %{version}-%{release}
Requires: elfutils-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : bzip2-dev
BuildRequires : flex
BuildRequires : flex-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32libcurl)
BuildRequires : pkgconfig(libcurl)
BuildRequires : procps-ng
BuildRequires : util-linux
BuildRequires : xz-dev
BuildRequires : xz-dev32
BuildRequires : zlib-dev
BuildRequires : zlib-dev32

%description
Elfutils is a collection of utilities, including stack (to show
backtraces), nm (for listing symbols from object files), size
(for listing the section sizes of an object or archive file),
strip (for discarding symbols), readelf (to see the raw ELF file
structures), elflint (to check for well-formed ELF files) and
elfcompress (to compress or decompress ELF sections).

%package bin
Summary: bin components for the elfutils package.
Group: Binaries
Requires: elfutils-license = %{version}-%{release}

%description bin
bin components for the elfutils package.


%package dev
Summary: dev components for the elfutils package.
Group: Development
Requires: elfutils-lib = %{version}-%{release}
Requires: elfutils-bin = %{version}-%{release}
Provides: elfutils-devel = %{version}-%{release}
Requires: elfutils = %{version}-%{release}

%description dev
dev components for the elfutils package.


%package dev32
Summary: dev32 components for the elfutils package.
Group: Default
Requires: elfutils-lib32 = %{version}-%{release}
Requires: elfutils-bin = %{version}-%{release}
Requires: elfutils-dev = %{version}-%{release}

%description dev32
dev32 components for the elfutils package.


%package lib
Summary: lib components for the elfutils package.
Group: Libraries
Requires: elfutils-license = %{version}-%{release}

%description lib
lib components for the elfutils package.


%package lib32
Summary: lib32 components for the elfutils package.
Group: Default
Requires: elfutils-license = %{version}-%{release}

%description lib32
lib32 components for the elfutils package.


%package license
Summary: license components for the elfutils package.
Group: Default

%description license
license components for the elfutils package.


%package locales
Summary: locales components for the elfutils package.
Group: Default

%description locales
locales components for the elfutils package.


%package man
Summary: man components for the elfutils package.
Group: Default

%description man
man components for the elfutils package.


%prep
%setup -q -n elfutils-0.183
cd %{_builddir}/elfutils-0.183
pushd ..
cp -a elfutils-0.183 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612810009
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used "
%configure  --program-prefix=eu- \
--with-zlib \
--with-lzma \
--without-bzlib \
--disable-debuginfod \
--disable-libdebuginfod
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure  --program-prefix=eu- \
--with-zlib \
--with-lzma \
--without-bzlib \
--disable-debuginfod \
--disable-libdebuginfod   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1612810009
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/elfutils
cp %{_builddir}/elfutils-0.183/COPYING %{buildroot}/usr/share/package-licenses/elfutils/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/elfutils-0.183/COPYING-GPLV2 %{buildroot}/usr/share/package-licenses/elfutils/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/elfutils-0.183/COPYING-LGPLV3 %{buildroot}/usr/share/package-licenses/elfutils/f45ee1c765646813b442ca58de72e20a64a7ddba
cp %{_builddir}/elfutils-0.183/doc/COPYING-GFDL %{buildroot}/usr/share/package-licenses/elfutils/4c0910524984176680adb6b68de639864bc1f8d0
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang elfutils
## Remove excluded files
rm -f %{buildroot}/usr/bin/addr2line
rm -f %{buildroot}/usr/bin/ar
rm -f %{buildroot}/usr/bin/ld
rm -f %{buildroot}/usr/bin/nm
rm -f %{buildroot}/usr/bin/objdump
rm -f %{buildroot}/usr/bin/ranlib
rm -f %{buildroot}/usr/bin/readelf
rm -f %{buildroot}/usr/bin/size
rm -f %{buildroot}/usr/bin/stack
rm -f %{buildroot}/usr/bin/strings
rm -f %{buildroot}/usr/bin/strip
rm -f %{buildroot}/usr/lib32/*.a
rm -f %{buildroot}/usr/lib64/libasm.a
rm -f %{buildroot}/usr/lib64/libdw.a
rm -f %{buildroot}/usr/lib64/libelf.a
rm -f %{buildroot}/usr/lib64/pkgconfig/libdebuginfod.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/32libdebuginfod.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/libdebuginfod.pc

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/eu-addr2line
/usr/bin/eu-ar
/usr/bin/eu-elfclassify
/usr/bin/eu-elfcmp
/usr/bin/eu-elfcompress
/usr/bin/eu-elflint
/usr/bin/eu-findtextrel
/usr/bin/eu-make-debug-archive
/usr/bin/eu-nm
/usr/bin/eu-objdump
/usr/bin/eu-ranlib
/usr/bin/eu-readelf
/usr/bin/eu-size
/usr/bin/eu-stack
/usr/bin/eu-strings
/usr/bin/eu-strip
/usr/bin/eu-unstrip

%files dev
%defattr(-,root,root,-)
/usr/include/dwarf.h
/usr/include/elfutils/elf-knowledge.h
/usr/include/elfutils/known-dwarf.h
/usr/include/elfutils/libasm.h
/usr/include/elfutils/libdw.h
/usr/include/elfutils/libdwelf.h
/usr/include/elfutils/libdwfl.h
/usr/include/elfutils/version.h
/usr/include/gelf.h
/usr/include/libelf.h
/usr/include/nlist.h
/usr/lib64/libasm.so
/usr/lib64/libdw.so
/usr/lib64/libelf.so
/usr/lib64/pkgconfig/libdw.pc
/usr/lib64/pkgconfig/libelf.pc
/usr/share/man/man3/elf_begin.3
/usr/share/man/man3/elf_clone.3
/usr/share/man/man3/elf_getdata.3
/usr/share/man/man3/elf_update.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libasm.so
/usr/lib32/libdw.so
/usr/lib32/libelf.so
/usr/lib32/pkgconfig/32libdw.pc
/usr/lib32/pkgconfig/32libelf.pc
/usr/lib32/pkgconfig/libdw.pc
/usr/lib32/pkgconfig/libelf.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libasm-0.183.so
/usr/lib64/libasm.so.1
/usr/lib64/libdw-0.183.so
/usr/lib64/libdw.so.1
/usr/lib64/libelf-0.183.so
/usr/lib64/libelf.so.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libasm-0.183.so
/usr/lib32/libasm.so.1
/usr/lib32/libdw-0.183.so
/usr/lib32/libdw.so.1
/usr/lib32/libelf-0.183.so
/usr/lib32/libelf.so.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/elfutils/4c0910524984176680adb6b68de639864bc1f8d0
/usr/share/package-licenses/elfutils/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/elfutils/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/elfutils/f45ee1c765646813b442ca58de72e20a64a7ddba

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/eu-elfclassify.1
/usr/share/man/man1/eu-readelf.1

%files locales -f elfutils.lang
%defattr(-,root,root,-)

