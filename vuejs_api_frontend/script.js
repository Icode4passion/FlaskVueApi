 

// var app = new Vue({
//     el:'#app',
//     data:{
//         movie_list: [],
//     },

//     mounted() {
//         axios
//             .get('http://127.0.0.1:5000/api/movies/')
//             .then(response => (
//                 this.movie_list = response.data
//                 ))
//             .catch(error =>(
//                 console.log(error)
//                 ));
//     }
// })

// import axios from 'axios';


// var app = new Vue({
//     el:"#app",
//     data (){
//         return {
//             movies = []
//         };
//     },
//     methods :{
//         getMovies(){
//             axios
//                 .get("http://127.0.0.1:5000/api/movies/")
//                 .then(response=>                     
//                     console.log(response.data)
//                     )
//         },
//     },
//     created(){
//         this.getMovies()
//     },
// })

// Our
var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data :{                   
            info : [],
            moviename : ""

       
    },    
    mounted () {        
        axios
            .get('http://127.0.0.1:5000/api/movies/')
            .then(response => (
                this.info = response.data
                ))
            .catch(error =>(
                console.log(error)
                ));
            },



            // search code is modified from https://morioh.com/p/7ef220f874dd
    computed :{

        filterMovieName : function(){
            var info = this.info;
            var moviename = this.moviename;

            if(!moviename){
                return info;           
             }
            searchstring = moviename.trim().toLowerCase() ;

            info = info.filter(function(item){
                if(item.movie_name.toLowerCase().indexOf(moviename)!==-1  || item.movie_director.toLowerCase().indexOf(moviename)!==-1){
                    return item;
                }
            })
            return info;
             }     


    }

    // computed :{
    //     filterMovieName(){
    //         return this.info.filter(item=>{
    //             return 
    //             item.movie_name.toLowerCase().startsWith(this.moviename.toLoweCase())
    //         })
    //     }
    // }

    

});