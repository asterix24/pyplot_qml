import QtQuick 2.13
import QtQuick.Controls 2.13
import QtCharts 2.13

ApplicationWindow {
    visible: true
    height: 480
    width: 600

    // Example taken from: https://doc.qt.io/qt-5/qtcharts-qmlchart-example.html
    ChartView {
        id: chart
        title: "Top-5 car brand shares in Finland"
        anchors.fill: parent
        legend.alignment: Qt.AlignBottom
        antialiasing: true

        LineSeries {
            id: lineSeries
            name: "LineSeries"
            XYPoint { x: 0; y: 0 }
            XYPoint { x: 1.1; y: 2.1 }
            XYPoint { x: 1.9; y: 3.3 }
            XYPoint { x: 2.1; y: 2.1 }
            XYPoint { x: 2.9; y: 4.9 }
            XYPoint { x: 3.4; y: 3.0 }
            XYPoint { x: 4.1; y: 3.3 }
            XYPoint { x: 7.1; y: 0.3 }
        }
    }
    Component.onCompleted: {

    }

    Timer {

         id: refreshTimer
         interval:1000 // 60 Hz
         running: true
         repeat: false
         onTriggered: {
             lineSeries.replace(2.9,4.9, 1.0, 1.0);
         }
     }
}
