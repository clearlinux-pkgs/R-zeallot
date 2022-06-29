#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-zeallot
Version  : 0.1.0
Release  : 31
URL      : https://cran.r-project.org/src/contrib/zeallot_0.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/zeallot_0.1.0.tar.gz
Summary  : Multiple, Unpacking, and Destructuring Assignment
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R

%description
unpacking, and destructuring assignment in R. The 
    operator unpacks the right-hand side of an assignment
    into multiple values and assigns these values to 
    variables on the left-hand side of the assignment.

%prep
%setup -q -c -n zeallot
cd %{_builddir}/zeallot

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641151558

%install
export SOURCE_DATE_EPOCH=1641151558
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library zeallot
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library zeallot
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library zeallot
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc zeallot || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/zeallot/DESCRIPTION
/usr/lib64/R/library/zeallot/INDEX
/usr/lib64/R/library/zeallot/LICENSE
/usr/lib64/R/library/zeallot/Meta/Rd.rds
/usr/lib64/R/library/zeallot/Meta/features.rds
/usr/lib64/R/library/zeallot/Meta/hsearch.rds
/usr/lib64/R/library/zeallot/Meta/links.rds
/usr/lib64/R/library/zeallot/Meta/nsInfo.rds
/usr/lib64/R/library/zeallot/Meta/package.rds
/usr/lib64/R/library/zeallot/Meta/vignette.rds
/usr/lib64/R/library/zeallot/NAMESPACE
/usr/lib64/R/library/zeallot/NEWS.md
/usr/lib64/R/library/zeallot/R/zeallot
/usr/lib64/R/library/zeallot/R/zeallot.rdb
/usr/lib64/R/library/zeallot/R/zeallot.rdx
/usr/lib64/R/library/zeallot/doc/index.html
/usr/lib64/R/library/zeallot/doc/unpacking-assignment.R
/usr/lib64/R/library/zeallot/doc/unpacking-assignment.Rmd
/usr/lib64/R/library/zeallot/doc/unpacking-assignment.html
/usr/lib64/R/library/zeallot/help/AnIndex
/usr/lib64/R/library/zeallot/help/aliases.rds
/usr/lib64/R/library/zeallot/help/paths.rds
/usr/lib64/R/library/zeallot/help/zeallot.rdb
/usr/lib64/R/library/zeallot/help/zeallot.rdx
/usr/lib64/R/library/zeallot/html/00Index.html
/usr/lib64/R/library/zeallot/html/R.css
/usr/lib64/R/library/zeallot/tests/testthat.R
/usr/lib64/R/library/zeallot/tests/testthat/test-collect.R
/usr/lib64/R/library/zeallot/tests/testthat/test-destructure.R
/usr/lib64/R/library/zeallot/tests/testthat/test-operator.R
/usr/lib64/R/library/zeallot/tests/testthat/test-pair-off.R
/usr/lib64/R/library/zeallot/tests/testthat/test-pipe.R
/usr/lib64/R/library/zeallot/tests/testthat/test-utils.R
