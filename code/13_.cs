
using System;
using System.IO;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace Program{

    //Solution:
    //find the line that would be a reflection if exactly one character would be different.

    public class Program{


        public static Int64 getVal(List<List<char>> matrix){

            int rows = matrix.Count, columns = matrix[0].Count;

            //checking columns
            for(int i = 1; i < columns; i++){//i = columns left to current column
                
                int columns_to_go = Math.Min(i, columns-i);
                int invalid_reflections = 0;

                //checking every column up to columns_to_go
                for(int j = 0; j < columns_to_go; j++){

                    //checking every row
                    for(int r = 0; r  < rows; r++){


                        //getting right values
                        char left = matrix[r][i-j-1];
                        char right = matrix[r][i+j];

                        if (left != right){//checking if it is not equal
                            invalid_reflections++;
                        }


                    }

                }

                if (invalid_reflections == 1){
                    return i;
                }


            }

            //no reflection found going horizontal, now going vertically
            for(int i = 1; i < rows; i++){

                int rows_to_go = Math.Min(i, rows-i);
                int invalid_reflections = 0;

                for(int j = 0; j < rows_to_go; j++){


                    for(int c = 0; c < columns; c++){


                        char left = matrix[i-j-1][c];
                        char right = matrix[i+j][c];

                        if(left != right){
                            invalid_reflections++;
                        }

                    }

                }

                if(invalid_reflections == 1) return 100*i;

            }

            return 0;

        }

        public static void Main(string[] args){

            string path = args[0];

            List<List<List<char>>> matrices = new List<List<List<char>>>();

            String line;
            try
            {
                List<List<char>> matrix = new List<List<char>>();
                StreamReader sr = new StreamReader(path);
                line = sr.ReadLine();
                //Continue to read until you reach end of file
                while (line != null)
                {

                    if((line.Contains("#") || line.Contains("."))){
                        List<char> linelist = new List<char>();
                        char[] charlist = line.ToCharArray();
                        linelist.AddRange(charlist);
                        matrix.Add(linelist);
                    }
                    else{
                        matrices.Add(matrix);
                        matrix = new List<List<char>>();
                    }
                    line = sr.ReadLine();
                }
                matrices.Add(matrix);
                //close the file
                sr.Close();
            }
            catch(Exception e)
            {
                Console.WriteLine("Exception: " + e.Message);
            }

            Int64 total = 0;

            foreach(List<List<char>> matrix in matrices){
                total += Program.getVal(matrix);
            }

            Console.WriteLine("{0}", total);

        }

    }

}