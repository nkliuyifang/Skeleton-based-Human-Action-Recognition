function PEI = calPEI(skeleton,type,RightHip,LeftHip,ORDER)

if size(skeleton,2) == 6
    skeleton1 = skeleton(:,1:3,:);
    skeleton2 = skeleton(:,4:6,:);
    skeleton = (skeleton1 + skeleton2)/2;
end

%% baseline
if type == 1
    x = squeeze(skeleton(:,1,:)); 
    y = squeeze(skeleton(:,2,:));
    z = squeeze(skeleton(:,3,:));

    min_x = min(min(x)); max_x = max(max(x));
    min_y = min(min(y)); max_y = max(max(y));
    min_z = min(min(z)); max_z = max(max(z));
    x = ((x-min_x)/(max_x - min_x+eps));
    y = ((y-min_y)/(max_y - min_y +eps));
    z = ((z-min_z)/(max_z - min_z+eps));   

    skeleton = cat(3,x,y,z);
    PEI = imresize(skeleton,[224,224]);
end

%% rotate
if type == 2
    skeleton = rotate_skeleton(skeleton,RightHip,LeftHip);
    
    x = squeeze(skeleton(:,1,:)); 
    y = squeeze(skeleton(:,2,:));
    z = squeeze(skeleton(:,3,:));

    min_x = min(min(x)); max_x = max(max(x));
    min_y = min(min(y)); max_y = max(max(y));
    min_z = min(min(z)); max_z = max(max(z));
    x = ((x-min_x)/(max_x - min_x+eps));
    y = ((y-min_y)/(max_y - min_y +eps));
    z = ((z-min_z)/(max_z - min_z+eps));   

    skeleton = cat(3,x,y,z);
    PEI = imresize(skeleton,[224,224]);
end

%% insert
if type == 3
    x = squeeze(skeleton(:,1,:)); 
    y = squeeze(skeleton(:,2,:));
    z = squeeze(skeleton(:,3,:));

    min_x = min(min(x)); max_x = max(max(x));
    min_y = min(min(y)); max_y = max(max(y));
    min_z = min(min(z)); max_z = max(max(z));
    x = ((x-min_x)/(max_x - min_x+eps));
    y = ((y-min_y)/(max_y - min_y +eps));
    z = ((z-min_z)/(max_z - min_z+eps));   

    skeleton = cat(3,x,y,z);

    INSERT = 5;
    PEI = [];
    for t = 1:size(skeleton,2)
        frame = squeeze(skeleton(:,t,:)); 
        pt = [];
        for k = 1:size(ORDER,1)
            st = frame(ORDER(k,1),:);
            ed = frame(ORDER(k,2),:);
            sub = ed - st;
            temp = [0:1/(INSERT+1):1]';
            temp = temp * sub;
            pt = [pt; temp+repmat(st,size(temp,1),1)];
        end
        if t == 1
            PEI = zeros(size(pt,1),3,size(skeleton,2));
        end
        PEI(:,:,t) = pt;
    end

    PEI = permute(PEI,[1 3 2]);
    PEI = imresize(PEI,[224,224]);
end

    
%% rotate and insert
if type == 4
    skeleton = rotate_skeleton(skeleton,RightHip,LeftHip);

    x = squeeze(skeleton(:,1,:)); 
    y = squeeze(skeleton(:,2,:));
    z = squeeze(skeleton(:,3,:));

    min_x = min(min(x)); max_x = max(max(x));
    min_y = min(min(y)); max_y = max(max(y));
    min_z = min(min(z)); max_z = max(max(z));
    x = ((x-min_x)/(max_x - min_x+eps));
    y = ((y-min_y)/(max_y - min_y +eps));
    z = ((z-min_z)/(max_z - min_z+eps));   

    skeleton = cat(3,x,y,z);

    INSERT = 5;
    PEI = [];
    for t = 1:size(skeleton,2)
        frame = squeeze(skeleton(:,t,:)); 
        pt = [];
        for k = 1:size(ORDER,1)
            st = frame(ORDER(k,1),:);
            ed = frame(ORDER(k,2),:);
            sub = ed - st;
            temp = [0:1/(INSERT+1):1]';
            temp = temp * sub;
            pt = [pt; temp+repmat(st,size(temp,1),1)];
        end
        if t == 1
            PEI = zeros(size(pt,1),3,size(skeleton,2));
        end
        PEI(:,:,t) = pt;
    end

    PEI = permute(PEI,[1 3 2]);
    PEI = imresize(PEI,[224,224]);
end