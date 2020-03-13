var createScene = require('gl-plot3d').createScene
var createLine  = require('gl-line3d')
//var loadnpy = require('npyjs')

// np_loader = new loadnpy()
// console.log(np_loader);
// np_loader.load('upload3d', (array, shape) => {
//     console.log("Load");
//     // `array` is a one-dimensional array of the raw data
//     // `shape` is a one-dimensional array that holds a numpy-style shape.
//     console.log(`You loaded an array with ${array.length} elements and ${shape.length} dimensions.`);
// });

// async function get_data(path){
//     var response = await fetch(path);
//     return response.json()
// }
// var data = await get_data("upload3d")
// console.log(dat)
//console.log(data)
const I   = [ 0,  1,  2,  0,  4,  5, 0, 7, 8, 9, 8, 11, 12, 8, 14, 15] //start points
const J   = [ 1,  2,  3,  4,  5,  6, 7, 8, 9, 10,11,12, 13, 14,15, 16] // end points
var LR  = [1,1,1,0,0,0,0, 0, 0, 0, 0, 0, 0, 1, 1, 1]

var data = [];
const container = document.querySelector('#container');
var scene = createScene({container: container});
document.querySelector('canvas').style.position = 'relative';



fetch("upload3d")
    .then (res => res.json())
    .then(json => {
        data = json;
        //console.log(data[0])
        drawFrame(data[40],scene)
    });

const drawFrame = (points,scene) => {
    for (i=0; i< I.length; i++){
        var x1 = points[I[i]][0]
        var y1 = points[I[i]][1]
        var z1 = points[I[i]][2]
        var x2 = points[J[i]][0]
        var y2 = points[J[i]][1]
        var z2 = points[J[i]][2]
        var linePlot = createLine({
            gl:        scene.gl,
            position:  [[x1,z1,y1],[x2,z2,y2]],
            lineWidth: 10,
            color:     [1,0,0]
            })
        scene.add(linePlot)
        // scene.bounds = [[-10,-10,-10], [10,10,10]]
    }
    var linePlot1 = createLine({
        gl:        scene.gl,
        position:  [[-1,0,0],[1,0,0]],
        lineWidth: 0,
        color:     [0,0,0]
        })

    var linePlot2 = createLine({
        gl:        scene.gl,
        position:  [[0,0,-1],[0,0,1]],
        lineWidth: 0,
        color:     [0,0,0]
        })
    
    var linePlot3 = createLine({
        gl:        scene.gl,
        position:  [[0,0,0],[0,2,0]],
        lineWidth: 0,
        color:     [0,0,0]
        })
    scene.add(linePlot1)
    scene.add(linePlot2)
    scene.add(linePlot3)
    
}

var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value;

slider.oninput = function() {
    output.innerHTML = this.value;
    // const canvas = document.querySelector('canvas');
    // document.querySelector('body').removeChild(canvas);
    // var scene = createScene();
    // document.querySelector('canvas').style.position = 'relative';
    scene.objects.length = 0
    // scene.bounds = [[-10,-10,-10], [10,10,10]]
    console.log(scene.objects)
    console.log("test")
    
    drawFrame(data[this.value], scene);
}

//console.log(data);
// const max_frame_id = data.length

// document.querySelector('#slider').addEventListener('drag', drawFrame(value))

// document.querySelector('#slide').addEventListener('', slide(value))
// const value = document.querySelector('#slide').value;
// slide(value);

// const slide = (frame_id) => {
//     return points = data[frame_id];
// }


