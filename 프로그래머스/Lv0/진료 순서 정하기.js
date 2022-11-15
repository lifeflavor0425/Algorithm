function solution(emergency) {
    var answer = [];
    let arr = [...emergency]
    let object={}
    let index =0;
    arr.sort((a,b)=>b-a)
    arr.forEach(e=>{
        object[e] = (index+=1)
    })
    answer = emergency.map(e=>object[e])
    return answer;
//      오름차순 인덱스에 + 1 
//     let sorted = emergency.slice().sort((a,b)=>b-a);
//     return emergency.map(v=>sorted.indexOf(v)+1);
}
