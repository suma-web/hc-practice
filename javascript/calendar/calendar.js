const dow = ['日','月','火','水','木','金','土'];
const today = new Date();


// calendarの出力パーツ
export function result(yyyy=today.getFullYear(), mm=today.getMonth()+1, dd=today.getDate()){
    // 初期設定
    const firstWeek = [];                           
    const secondWeek = [];                          
    const thirdWeek = [];
    const forthWeek = [];
    const fifthWeek = [];
    const sixWeek = [];
    let monthFirstDays = '';                        
    let monthSecondDays = '';                       
    let monthThirdDays = '';
    let monthFourthDays = '';
    let monthFifthDays = '';
    let monthSixDays = '';

    // 月初の日付
    const firstDay = new Date(yyyy, mm-1, 1);
    const firstDowNum = firstDay.getDay();
    const fisrtWeekLastNumber = 7 - firstDowNum

    
    // 第1週目
    for (let i=0; i<firstDowNum; i++){
        firstWeek.push(' '); 
    }

    for(let i=1; i<=fisrtWeekLastNumber; i++){
        if (dd===i && mm === today.getMonth()+1){
            firstWeek.push(`[${i}]`);
        }else{
            firstWeek.push(i);
        }
    }

    firstWeek.forEach((day) => {
        monthFirstDays += ` ${day} `; 
    });


    // 第2週目
    for(let i=firstWeek[6]+1; i<=firstWeek[6]+7; i++){
        if (dd === i && mm === today.getMonth()+1){
            secondWeek.push(`[${i}]`);
        }else{
            secondWeek.push(i);
        }
    }

    secondWeek.forEach((day) => {
        if (day>=10){
            monthSecondDays += `${day} `;
        }else{
            monthSecondDays += ` ${day} `;
        } 
    });


    //第3週目
    for(let i=secondWeek[6]+1; i<=secondWeek[6]+7; i++){
        if (dd === i && mm === today.getMonth()+1){
            thirdWeek.push(`[${i}]`);
        }else{
            thirdWeek.push(i); 
        }
    }

    thirdWeek.forEach((day) => {
        monthThirdDays += `${day} `; 
    });

    //第4週目
    const monthLastDay = new Date(yyyy, mm, 0).getDate();
    

    for(let i=thirdWeek[6]+1; i<=thirdWeek[6]+7; i++){
        if (dd === i && mm === today.getMonth()+1){
            forthWeek.push(`[${i}]`);
        } else if(monthLastDay < i) {
            break;
        } else {
            forthWeek.push(i);
        }
    }

    forthWeek.forEach((day) => {
        monthFourthDays += `${day} `; 
    });

    //第5週目
    for(let i=forthWeek[6]+1; i<=forthWeek[6]+7; i++){
        if (dd === i && mm === today.getMonth()+1){
            fifthWeek.push(`[${i}]`);
        } else if(monthLastDay < i) {
            break;
        } else {
            fifthWeek.push(i);
        }
    }

    fifthWeek.forEach((day) => {
        monthFifthDays += `${day} `; 
    });

    //第6週目
    for(let i=fifthWeek[6]+1; i<=fifthWeek[6]+7; i++){
        if (dd === i && mm === today.getMonth()+1 ){
            sixWeek.push(`[${i}]`);
        } else if(monthLastDay < i) {
            break;
        } else {
            sixWeek.push(i);
        }
    }

    sixWeek.forEach((day) => {
        monthSixDays += `${day} `; 
    });

    console.log(`       ${mm}月 ${yyyy}`);
    console.log(`${dow.join(' ')}`);
    console.log(monthFirstDays);
    console.log(monthSecondDays);
    console.log(monthThirdDays);
    console.log(monthFourthDays);
    console.log(monthFifthDays);
    console.log(monthSixDays);
}