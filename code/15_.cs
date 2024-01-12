
using System;
using System.IO;
using System.Collections.Generic;

namespace Program{

    class Program{

        protected class StringValuePair{

            public string label = null;
            public int focus = 0;

            public StringValuePair(string l, int f){
                label = l;
                focus = f;
            }

        }

        protected static Int64 Hash(string code){
            
            Int64 val = 0;

            foreach(char c in code){
                val += (Int64)c;
                val *= 17;
                val %= 256;
            }

            return val;
        }

        protected static string[] Process(string value){

            int count = 0;
            for(int i = 0; i < value.Length; i++){
                if (value[i] == '=' || value[i] == '-'){
                    count = i;
                    break;
                }
            }
            return new string[]{value.Substring(0, count), value.Substring(count, 1), value.Substring(count+1, (value.Length - count - 1))};

        }

        protected static Int64 CalculateFocus(string[] values){

            List<List<StringValuePair>> L = new List<List<StringValuePair>>();
            for(int i = 0; i < 256; i++){
                L.Add(new List<StringValuePair>());
            }

            foreach(string val in values){

                string[] processed = Program.Process(val);
                string label = processed[0], operation = processed[1];
                int focus = -1;
                if (processed[2].Length > 0){
                    focus = Convert.ToInt32(processed[2]);
                }

                int hashval = Convert.ToInt32(Program.Hash(label));
                //got the hashed box, now doing the operation

                //checking and removing has to be done in both parts
                List<StringValuePair> box = L[hashval];

                int removeIndex = -1;
                int counter = 0;
                foreach(StringValuePair svp in box){

                    if (svp.label == label){
                        removeIndex = counter;
                        break;
                    }
                    counter++;

                }

                
                if(operation == "="){
                    //additionally adding
                    if (removeIndex == -1){
                        box.Add(new StringValuePair(label, focus));
                    }
                    else{
                        StringValuePair svp = box[removeIndex];
                        svp.focus = focus;
                    }
                }
                else{
                    //- operation
                    if (removeIndex != -1){
                         box.RemoveAt(removeIndex);
                    }
                }



            }

            Int64 summe = 0;
            int count = 0;
            foreach(List<StringValuePair> box in L){

                for(int i = 0; i < box.Count; i++){

                    summe += (count+1)*(i+1)*(box[i].focus);
                }
                count++;

            }


            return summe;

        }
        public static void Main(string[] args){

            string path = args[0];
            StreamReader sr = new StreamReader(path);
            string line;

            line = sr.ReadLine();
            sr.Close();
            string[] data = line.Split(',');

            Int64 summe = CalculateFocus(data);
            Console.WriteLine(summe);




        }

    }

}