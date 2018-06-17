function preLoadImg() {
    var imgs = ['00.jpeg', '01.jpg', '02.gif'];
    res = imgs.map(function (item, value) {
        var img = new Image();
        img.src = item;
        return img;
    })
    return res
}

var count = 0;
imgs = preLoadImg()
console.log('cao');
var frame_2 = document.getElementById('frame-2')
frame_2.appendChild(imgs[0]);
imgs[0].width = 300
var button_1 = document.getElementsByTagName('button')[0]
var button_2 = document.getElementsByTagName('button')[3]
button_1.disable = true
button_1.style.color = 'grey'


function next(e) {
    if (count < 2) {
        button_1.style.color = null;
        console.log('next()', res[count])
        res.id = count
        var img = document.getElementsByTagName('img')[0]
        img.width = 300
        frame_2.removeChild(img)
        frame_2.appendChild(res[count + 1])
        count++
        if (count == 2) {
            e.style.color = 'grey'
        }
    } else {
        e.disable = true
        e.style.color = 'grey'
    }
}


function last(e) {
    console.log(count)
    if (count > 0) {
        button_2.style.color = null;
        var img = document.getElementsByTagName('img')[0]
        img.width = 300
        frame_2.removeChild(img)
        frame_2.appendChild(res[count - 1])
        count--;
        if (count == 0) {
            e.style.color = 'grey'
        }
    } else {
        e.disable = true
        e.style.color = 'grey'
    }
}


function enlarge() {
    var img = document.getElementsByTagName('img')[0]
    img.width += 10
}


function reduce() {
    var img = document.getElementsByTagName('img')[0]
    if (img.width>100){
        img.width -= 10
    }
}