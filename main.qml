import QtQuick 2.13
import QtQuick.Controls 2.13
import QtCharts 2.13
import myseries 1.0

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

        ValueAxis {
            id: axisX
            min: 0
            max: 20
        }


        ValueAxis {
            id: axisY
            min: 0
            max: 20
        }

        LineSeries{
            id: line
            axisX: axisX
            axisY: axisY
        }

        VXYModelMapper {
            id: modelMapper
            model: Series {
                id: series
            }
            series: line
            xColumn: 0
            yColumn: 1
        }
    }

    Timer {

         id: refreshTimer
         interval:1000 // 60 Hz
         running: true
         repeat: true
         onTriggered: {
             series.reloadModel()
            //  lineSeries.replace(2.9,4.9, 1.0, 1.0);
         }
     }
}
