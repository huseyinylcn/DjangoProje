const firebaseConfig = {
    apiKey: "AIzaSyDct6Llp5nINGWnp6t-NBsxWin1riyccig",
    authDomain: "aglsistem-71590.firebaseapp.com",
    databaseURL: "https://aglsistem-71590-default-rtdb.firebaseio.com",
    projectId: "aglsistem-71590",
    storageBucket: "aglsistem-71590.appspot.com",
    messagingSenderId: "510994901595",
    appId: "1:510994901595:web:c12a5b74517b3a2c4ced7e",
    measurementId: "G-MFWNV461CE"
  };

firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();

db.collection("Bursa_Prop").where('gelenzaman','>','2023-02-05-00-00-39').get().then((snapshot)=>{
snapshot.docs.forEach((snapp)=>{

  console.log(snapp.data())
  
})

 })

//  
  


  // var margin = {top: 10, right: 30, bottom: 100, left: 60}
  // var width = 500- margin.left - margin.right;
  

  
  //     height = 300 - margin.top - margin.bottom;
  
  // // append the svg object to the body of the page
  // var svg = d3.select("#my_dataviz")
  //   .append("svg")
  //     .attr("width", width + margin.left + margin.right)
  //     .attr("height", height + margin.top + margin.bottom)
      
  //   .append("g")
  //     .attr("transform",
  //           "translate(" + margin.left + "," + margin.top + ")");
        
  
  //           const x = d3.scaleBand()
  //           .range([ 0, width ])
  //           .paddingInner(0.1)
  //           .paddingOuter(0.2);;
  //        const xx = svg.append("g")
  //           .attr("transform", "translate(0," + height + ")")
           
            
        
  //         // Add Y axis
  //         const y = d3.scaleLinear()
  //           .range([ height, 0 ]);
  //        const yy = svg.append("g")
  //        const rr =svg.append("path")   
  // let dat = [];     
  
  // db.collection("Bursa_Prop").onSnapshot((snapshot) => {
  //   snapshot.docChanges().forEach((change) => {
  //   if (change.type === 'added') {
  //   dat.push(change.doc.data());
  //   update(dat);
  //   }
  //   });
  //   });
    
 
  
  
  
  // function update(dat){
   
  //   // console.log(typeof dat[0]["veri"])
  // if(dat.length>10000){
  //   dat.shift();
  // }
  // x.domain(dat.map(d=>d.time ))
  // y.domain([d3.min(dat, d => d.veri)-0.3, d3.max(dat, d => d.veri)+1])
  
  // xx.call(d3.axisBottom(x)
  // .tickValues(x.domain().filter((d,i) => !(i % Math.ceil(dat.length / 10)))))
  // .selectAll("text")
  //     .attr("y", "10")
  //     .attr("x", "-5")
  //     .attr("text-anchor", "end")
  //     .attr("transform", "rotate(-40)")
  
  // yy.call(d3.axisLeft(y));
  
  //   rr.datum(dat)
  //   .attr("fill", "none")
  //   .attr("stroke",  d => d.veri > 1000 ? "red" : "black")
  //   .attr("stroke-width", 0.8)
  //   .attr("d", d3.line()
  //     .x(function(d) { return x(d.time) })
  //     .y(function(d) { return y(d.veri) })
  //     )
  // }
  
  
  
  function showForm() {
    const form = document.getElementById("loginForm");
    form.style.display = "block";
  }



  function none(){
    document.getElementById("loginForm").style.display="none";

  }