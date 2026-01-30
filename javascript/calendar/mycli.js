import {showMonthYear} from './calendar.js';
import {calendarResult} from './calendar.js';


const arg = process.argv.slice(2);
const command = arg[0];
const option = Number(arg[1]);

if (1>option || option>12){
    console.log('不正な入力エラー');
}else{
    if (command === '-m' && (1<=option && option<=12)){
            const mm = option;
            const yyyy = new Date().getFullYear();

            showMonthYear(yyyy,mm);
            calendarResult(yyyy, mm);
    }else{
        showMonthYear();
        calendarResult();
    }
}
