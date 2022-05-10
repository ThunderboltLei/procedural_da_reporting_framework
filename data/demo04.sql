-- auto-generated definition
create table core_indicator
(
    indicator_en       varchar(80)                         null,
    indicator_val         varchar(80)                         null,
    indicator_cn        varchar(200)                        null,
    create_time timestamp default CURRENT_TIMESTAMP null,
    modify_time timestamp default CURRENT_TIMESTAMP null
);

insert into core_indicator(indicator_en, indicator_val, indicator_cn)
values ('DAU', '10W :star:', '三端矩阵 DAU'),
       ('UV', '10W :moon:', '三端矩阵 UV'),
       ('Video_Time', '10W :fire:', '三端矩阵播放时长');


create table users
(
    id          int auto_increment primary key,
    username    varchar(50) not null,
    create_time timestamp(3) null,
    modify_time timestamp(3) null
);



