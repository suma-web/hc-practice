const dow = ['日','月','火','水','木','金','土'];
const today = new Date();


export function showMonthYear(yyyy=today.getFullYear(), mm=today.getMonth()+1){
    console.log(`      ${mm}月 ${yyyy}\n${dow.join(' ')}`);
}

// calendarの出力パーツ
export function calendarResult(yyyy=today.getFullYear(), mm=today.getMonth()+1){
    // 初期設定
    const arrayDays = [];
    const firstDayDowNum = new Date(yyyy, mm-1).getDay();

    // 該当月の日数取得
    const monthDays = new Date(yyyy, mm, 0).getDate();

    // 取得日数を挿入
    for (let i = 0; i < firstDayDowNum + monthDays; i++) {
        if (i < firstDayDowNum) {
            arrayDays.push("");
        } else {
            arrayDays.push(i - firstDayDowNum + 1);
        }
    }

    arrayDays.forEach((day,index) => {
        process.stdout.write(day.toString().padStart(2, " ") + " ");

        if ((index + 1) % 7 === 0) {
            process.stdout.write("\n");
        }
    });

    return arrayDays
}