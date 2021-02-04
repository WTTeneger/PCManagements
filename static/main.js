actives = true;

function TakeKay(Key) {
    console.log(Key);
    var re = /(Volumes)+/i;
    if (re.test(Key)) {
        b = document.getElementById('VolumesID').value;
        console.log(b);
        document.getElementById('lbl').innerHTML = b;
        Pulls('Volumes' + b);
    } else {
        if (Key == "SS") {
            dc = document.getElementById('SS');
            console.log(dc);
            if (actives == false) {
                dc.classList.add('ActiveMusic')
                actives = true;
                dc.innerHTML = '▶'
            } else {
                actives = false;
                dc.classList.remove('ActiveMusic');
                dc.innerHTML = '||'
            }

        }
        Pulls(Key);
    }
}

function Pulls(Keys) {
    urls = 'http://192.168.3.2:8000/ClockBut/'
    urls += Keys
    dats = ''
    $.ajax({
        type: "POST",
        url: urls,
        async: false,
        success: function(data) {
            console.log('Response - ', data)
            dats = data
        }
    });
    return (dats)
};