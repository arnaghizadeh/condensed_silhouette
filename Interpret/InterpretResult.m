clear;
clc;
fid1 = fopen('out.txt','r');
fid2 = fopen('out.m','w'); %# open new csv file
fprintf(fid2,'clear;\n');
fprintf(fid2,'clc;\n');
fprintf(fid2,'format long g\n');
fprintf(fid2,'counterAll = 0;\n');
fprintf(fid2,'sumAll = 0.0;\n');
fprintf(fid2,'maxAccuracy = -1;\n');
fprintf(fid2,'allAccuracies = zeros(100,1);\n');%change based on the number of experiments

while ~feof(fid1)
    line = fgetl(fid1);
    %strcmp(line,'*********Final Results*********')
    if strcmp(line,'*********Analyse of final results*********')==1
        line = fgets(fid1);%skip the first line
        line1 = fgets(fid1);
        line2 = fgets(fid1);
        line3 = fgets(fid1);
        line4 = fgets(fid1);
        fprintf(fid2,'%s',line1); %# write the line to the new file
        fprintf(fid2,'%s',line2); %# write the line to the new file
        fprintf(fid2,'%s',line3); %# write the line to the new file
        fprintf(fid2,'%s',line4); %# write the line to the new file
        fprintf(fid2,'sumAll = sumAll + (1 - missrateTot1);\n');
        fprintf(fid2,'counterAll = counterAll + 1;\n');   
        fprintf(fid2,'allAccuracies(counterAll) = (1 - missrateTot1)*100;\n'); 
        fprintf(fid2,'if maxAccuracy < (1 - missrateTot1)\n'); 
        fprintf(fid2,'    maxAccuracy = (1 - missrateTot1);\n'); 
        fprintf(fid2,'end \n'); 
    end
    
end 
fprintf(fid2,'cumAccuracy = sumAll*100,\n');
fprintf(fid2,'meanAccuracy = (sumAll/counterAll)*100,\n');
fprintf(fid2,'maxAccuracy = maxAccuracy*100\n');
%STD calculation
fprintf(fid2,'variance = 0;\n');
fprintf(fid2,'for idx = 1:numel(allAccuracies)\n');
fprintf(fid2,'    element = allAccuracies(idx);\n');
fprintf(fid2,'    variance= variance + ((meanAccuracy - element)^2);\n');
fprintf(fid2,'end\n');
fprintf(fid2,'variance = variance/counterAll;\n');
fprintf(fid2,'STD = sqrt(variance)\n');