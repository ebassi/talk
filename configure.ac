AC_INIT([talk], [1.0], [ebassi@gnome.org])
AC_CONFIG_SRCDIR([talk/__init__.py])
AC_CONFIG_HEADERS(config.h)
AC_CONFIG_MACRO_DIR([m4])

AM_INIT_AUTOMAKE
GNOME_COMMON_INIT

AM_MAINTAINER_MODE
AM_DISABLE_STATIC
AM_PROG_LIBTOOL
AC_SUBST(ACLOCAL_AMFLAGS, "$ACLOCAL_FLAGS -I m4")
AC_PROG_CC

dnl ****************************************************************************
dnl * Pkg-Config
dnl ****************************************************************************
AC_CHECK_PROG(HAVE_PKGCONFIG, pkg-config, yes, no)
if test "x$HAVE_PKGCONFIG" = "xno"; then
  AC_MSG_ERROR(you need to have pkgconfig installed !)
fi

dnl ****************************************************************************
dnl * Python 2.5
dnl ****************************************************************************
AM_PATH_PYTHON(2.5)
AM_CHECK_PYTHON_HEADERS(,[AC_MSG_ERROR(could not find Python headers)])

dnl ****************************************************************************
dnl * Write the values of various paths in defs.py
dnl ****************************************************************************
AC_SUBST(VERSION)
AC_SUBST(PACKAGE)

AS_AC_EXPAND(DATADIR, $datarootdir)
AC_SUBST(DATADIR)

AS_AC_EXPAND(LIBDIR, $libdir)
AC_SUBST(LIBDIR)

AS_AC_EXPAND(PYTHONDIR, $pythondir)
AC_SUBST(PYTHONDIR)
		
PKG_CHECK_MODULES(TALK,
	gtk+-2.0			>= 2.10
	pygtk-2.0			>= 2.10
	pygobject-2.0			>= 2.10
        pyclutter-0.6                   >= 0.6.0
)
AC_SUBST(TALK_CFLAGS)
AC_SUBST(TALK_LIBS)

AC_MSG_CHECKING([for cluttergtk module])
if AC_RUN_LOG([$PYTHON -c '
try:
    from clutter import cluttergtk
except ImportError, e:
    if str(e).find("cluttergtk") >= 0:
          raise
except:
    pass
']); then
  AC_MSG_RESULT([yes])
else
  AC_MSG_RESULT([no])
  AC_MSG_ERROR([cluttergtk Python module required to build talk])
fi

AC_MSG_CHECKING([for tidy module])
if AC_RUN_LOG([$PYTHON -c '
try:
    from clutter import tidy
except ImportError, e:
    if str(e).find("tidy") >= 0:
          raise
except:
    pass
']); then
  AC_MSG_RESULT([yes])
else
  AC_MSG_RESULT([no])
  AC_MSG_ERROR([tidy Python module required to build talk])
fi

dnl ****************************************************************************
dnl * PyGTK Codegen and defs files
dnl ****************************************************************************
AC_PATH_PROG(PYGTK_CODEGEN, pygtk-codegen-2.0, no)
if test "x$PYGTK_CODEGEN" = xno; then
  AC_MSG_ERROR(could not find pygtk-codegen-2.0 script)
fi

AC_MSG_CHECKING(for pygtk defs)
PYGTK_DEFSDIR=`$PKG_CONFIG --variable=defsdir pygtk-2.0`
AC_SUBST(PYGTK_DEFSDIR)
AC_MSG_RESULT($PYGTK_DEFSDIR)

AC_OUTPUT([
Makefile
talk/Makefile
talk/defs.py
data/Makefile
])

echo
echo $PACKAGE v$VERSION
echo

echo "Now type make to compile"
echo "Then su to root and type: make install"
echo
