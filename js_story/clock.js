const min_hand = document.querySelector('.min_clock');
const hour_hand = document.querySelector('.hour_clock');
const second_hand = document.querySelector('.second_clock');


min_clock
hour_clock
second_clock

function get_time(){
    const today = new Date();
    const seconds = today.getSeconds();
    const secondsDegress = ((seconds/60)*360) + 90;
    second_hand.style.transform = 'rotate(${secondsDegress}deg)';
    const minute = today.getMinutes();
    const minuteDegress = ((minute/60)*360) + ((seconds/60)*6) + 90;
    min_hand.style.transform = 'rotate(${minuteDegress}deg)';
    const hour = today.getHours();
    const hourDegress = ((hour/60)*360) + ((minute/60)*30) + 90;
    hour_hand.style.transform = 'rotate(${hourDegress}deg)';
}
setInterval(get_time, 1000);

get_time();