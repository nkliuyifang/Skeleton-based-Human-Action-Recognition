function S = rotate_skeleton(S,RightHip,LeftHip)

S0 = mean(S,3);
cur = [S0(:,1),S0(:,3)];
pt1 = cur(RightHip,:);
pt2 = cur(LeftHip,:);
old = pt2 - pt1;
new = [0 1];
cosj = dot(old,new)/(norm(old)*norm(new));
sinj = (1-cosj^2)^0.5;
R = [cosj   -sinj
     sinj    cosj];

for t = 1:size(S,3)
    skeleton = S(:,:,t);
    
    for k = 1:size(skeleton,1)
        old = skeleton(k,:);
        old = [old(:,1),old(:,3)];
        new = R*old';
        skeleton(k,1) = new(1,1);
        skeleton(k,3) = new(2,1);
    end
    S(:,:,t) = skeleton;
end

end


function plot_skeleton(skeleton)
    J = [ 1 2 3 3 5 6 7 3  9 10 11  1  1 13 14 15 17 18 19 13;
     2 3 4 5 6 7 8 9 10 11 12 13 17 14 15 16 18 19 20 17];
    figure;
    for k = 1:size(J,2)
        hold on;
        line([skeleton(J(1,k),1) skeleton(J(2,k),1)], [skeleton(J(1,k),2) skeleton(J(2,k),2)]); 
        if k == 20
            pt1 = skeleton(J(1,k),:);
            pt2 = skeleton(J(2,k),:);
            hold on;
            line([skeleton(J(1,k),1) skeleton(J(2,k),1)], [skeleton(J(1,k),2) skeleton(J(2,k),2)], 'color', 'r'); 
        end
    end
end

function R=fcn_RotationFromTwoVectors(A, B) 
    v = cross(A,B); 
    ssc = [0 -v(3) v(2); v(3) 0 -v(1); -v(2) v(1) 0]; 
    R = eye(3) + ssc + ssc^2*(1-dot(A,B))/(norm(v))^2;
end