# -*- coding: utf-8 -*-

# Resource object code
#
# Created: gio mar 4 10:40:15 2021
#      by: The Resource Compiler for PySide2 (Qt v5.13.0)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x02\xe7\
i\
mport QtQuick 2.\
13\x0aimport QtQuic\
k.Controls 2.13\x0a\
import QtCharts \
2.13\x0a\x0aApplicatio\
nWindow {\x0a    vi\
sible: true\x0a\x0a   \
 // Example take\
n from: https://\
doc.qt.io/qt-5/q\
tcharts-qmlchart\
-example.html\x0a  \
  ChartView {\x0a  \
      id: chart\x0a\
        title: \x22\
Top-5 car brand \
shares in Finlan\
d\x22\x0a        ancho\
rs.fill: parent\x0a\
        legend.a\
lignment: Qt.Ali\
gnBottom\x0a       \
 antialiasing: t\
rue\x0a\x0a\x0a        Li\
neSeries {\x0a     \
       id: lineS\
eries\x0a          \
  name: \x22LineSer\
ies\x22\x0a           \
 XYPoint { x: 0;\
 y: 0 }\x0a        \
    XYPoint { x:\
 1.1; y: 2.1 }\x0a \
           XYPoi\
nt { x: 1.9; y: \
3.3 }\x0a          \
  XYPoint { x: 2\
.1; y: 2.1 }\x0a   \
         XYPoint\
 { x: 2.9; y: 4.\
9 }\x0a            \
XYPoint { x: 3.4\
; y: 3.0 }\x0a     \
       XYPoint {\
 x: 4.1; y: 3.3 \
}\x0a        }\x0a    \
}\x0a\x0a}\x0a\x0a\
"

qt_resource_name = b"\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
