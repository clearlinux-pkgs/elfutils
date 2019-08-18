#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFC57E3CCACD99A78 (mjw@gnu.org)
#
%define keepstatic 1
Name     : elfutils
Version  : 0.177
Release  : 65
URL      : https://sourceware.org/elfutils/ftp/0.177/elfutils-0.177.tar.bz2
Source0  : https://sourceware.org/elfutils/ftp/0.177/elfutils-0.177.tar.bz2
Source1 : https://sourceware.org/elfutils/ftp/0.177/elfutils-0.177.tar.bz2.sig
Summary  : A collection of utilities and DSOs to handle ELF files and DWARF data
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ GPL-3.0 GPL-3.0+ LGPL-3.0 LGPL-3.0+
Requires: elfutils-bin = %{version}-%{release}
Requires: elfutils-lib = %{version}-%{release}
Requires: elfutils-license = %{version}-%{release}
Requires: elfutils-locales = %{version}-%{release}
BuildRequires : bison
BuildRequires : bzip2-dev
BuildRequires : flex
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : procps-ng
BuildRequires : util-linux
BuildRequires : xz-dev
BuildRequires : xz-dev32
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
Patch1: cve-2018-8769.nopatch

%description
Elfutils is a collection of utilities, including stack (to show
backtraces), nm (for listing symbols from object files), size
(for listing the section sizes of an object or archive file),
strip (for discarding symbols), readelf (to see the raw ELF file
structures), elflint (to check for well-formed ELF files) and
elfcompress (to compress or decompress ELF sections).
Also included are helper libraries which implement DWARF, ELF,
and machine-specific ELF handling and process introspection.

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


%package extras
Summary: extras components for the elfutils package.
Group: Default

%description extras
extras components for the elfutils package.


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


%package staticdev
Summary: staticdev components for the elfutils package.
Group: Default
Requires: elfutils-dev = %{version}-%{release}

%description staticdev
staticdev components for the elfutils package.


%prep
%setup -q -n elfutils-0.177
pushd ..
cp -a elfutils-0.177 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1566160539
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure  --program-prefix=eu- --with-zlib  --with-lzma --without-bzlib
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32"
%configure  --program-prefix=eu- --with-zlib  --with-lzma --without-bzlib   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1566160539
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/elfutils
cp COPYING %{buildroot}/usr/share/package-licenses/elfutils/COPYING
cp COPYING-GPLV2 %{buildroot}/usr/share/package-licenses/elfutils/COPYING-GPLV2
cp COPYING-LGPLV3 %{buildroot}/usr/share/package-licenses/elfutils/COPYING-LGPLV3
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
/usr/include/*.h
/usr/include/elfutils/elf-knowledge.h
/usr/include/elfutils/known-dwarf.h
/usr/include/elfutils/libasm.h
/usr/include/elfutils/libdw.h
/usr/include/elfutils/libdwelf.h
/usr/include/elfutils/libdwfl.h
/usr/include/elfutils/libebl.h
/usr/include/elfutils/version.h
/usr/lib64/libasm.so
/usr/lib64/libdw.so
/usr/lib64/libelf.so
/usr/lib64/pkgconfig/libdw.pc
/usr/lib64/pkgconfig/libelf.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libasm.so
/usr/lib32/libdw.so
/usr/lib32/libelf.so
/usr/lib32/pkgconfig/32libdw.pc
/usr/lib32/pkgconfig/32libelf.pc
/usr/lib32/pkgconfig/libdw.pc
/usr/lib32/pkgconfig/libelf.pc

%files extras
%defattr(-,root,root,-)
/usr/lib64/elfutils/libebl_alpha-0.177.so
/usr/lib64/elfutils/libebl_alpha.so
/usr/lib64/elfutils/libebl_arm-0.177.so
/usr/lib64/elfutils/libebl_arm.so
/usr/lib64/elfutils/libebl_bpf-0.177.so
/usr/lib64/elfutils/libebl_bpf.so
/usr/lib64/elfutils/libebl_ia64-0.177.so
/usr/lib64/elfutils/libebl_ia64.so
/usr/lib64/elfutils/libebl_m68k-0.177.so
/usr/lib64/elfutils/libebl_m68k.so
/usr/lib64/elfutils/libebl_ppc-0.177.so
/usr/lib64/elfutils/libebl_ppc.so
/usr/lib64/elfutils/libebl_ppc64-0.177.so
/usr/lib64/elfutils/libebl_ppc64.so
/usr/lib64/elfutils/libebl_riscv-0.177.so
/usr/lib64/elfutils/libebl_riscv.so
/usr/lib64/elfutils/libebl_s390-0.177.so
/usr/lib64/elfutils/libebl_s390.so
/usr/lib64/elfutils/libebl_sh-0.177.so
/usr/lib64/elfutils/libebl_sh.so
/usr/lib64/elfutils/libebl_sparc-0.177.so
/usr/lib64/elfutils/libebl_sparc.so
/usr/lib64/elfutils/libebl_tilegx-0.177.so
/usr/lib64/elfutils/libebl_tilegx.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/elfutils/libebl_aarch64-0.177.so
/usr/lib64/elfutils/libebl_aarch64.so
/usr/lib64/elfutils/libebl_csky-0.177.so
/usr/lib64/elfutils/libebl_csky.so
/usr/lib64/elfutils/libebl_i386-0.177.so
/usr/lib64/elfutils/libebl_i386.so
/usr/lib64/elfutils/libebl_x86_64-0.177.so
/usr/lib64/elfutils/libebl_x86_64.so
/usr/lib64/libasm-0.177.so
/usr/lib64/libasm.so.1
/usr/lib64/libdw-0.177.so
/usr/lib64/libdw.so.1
/usr/lib64/libelf-0.177.so
/usr/lib64/libelf.so.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/elfutils/libebl_aarch64-0.177.so
/usr/lib32/elfutils/libebl_aarch64.so
/usr/lib32/elfutils/libebl_alpha-0.177.so
/usr/lib32/elfutils/libebl_alpha.so
/usr/lib32/elfutils/libebl_arm-0.177.so
/usr/lib32/elfutils/libebl_arm.so
/usr/lib32/elfutils/libebl_bpf-0.177.so
/usr/lib32/elfutils/libebl_bpf.so
/usr/lib32/elfutils/libebl_csky-0.177.so
/usr/lib32/elfutils/libebl_csky.so
/usr/lib32/elfutils/libebl_i386-0.177.so
/usr/lib32/elfutils/libebl_i386.so
/usr/lib32/elfutils/libebl_ia64-0.177.so
/usr/lib32/elfutils/libebl_ia64.so
/usr/lib32/elfutils/libebl_m68k-0.177.so
/usr/lib32/elfutils/libebl_m68k.so
/usr/lib32/elfutils/libebl_ppc-0.177.so
/usr/lib32/elfutils/libebl_ppc.so
/usr/lib32/elfutils/libebl_ppc64-0.177.so
/usr/lib32/elfutils/libebl_ppc64.so
/usr/lib32/elfutils/libebl_riscv-0.177.so
/usr/lib32/elfutils/libebl_riscv.so
/usr/lib32/elfutils/libebl_s390-0.177.so
/usr/lib32/elfutils/libebl_s390.so
/usr/lib32/elfutils/libebl_sh-0.177.so
/usr/lib32/elfutils/libebl_sh.so
/usr/lib32/elfutils/libebl_sparc-0.177.so
/usr/lib32/elfutils/libebl_sparc.so
/usr/lib32/elfutils/libebl_tilegx-0.177.so
/usr/lib32/elfutils/libebl_tilegx.so
/usr/lib32/elfutils/libebl_x86_64-0.177.so
/usr/lib32/elfutils/libebl_x86_64.so
/usr/lib32/libasm-0.177.so
/usr/lib32/libasm.so.1
/usr/lib32/libdw-0.177.so
/usr/lib32/libdw.so.1
/usr/lib32/libelf-0.177.so
/usr/lib32/libelf.so.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/elfutils/COPYING
/usr/share/package-licenses/elfutils/COPYING-GPLV2
/usr/share/package-licenses/elfutils/COPYING-LGPLV3

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libebl.a

%files locales -f elfutils.lang
%defattr(-,root,root,-)

