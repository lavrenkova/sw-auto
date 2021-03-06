﻿using MongoDB.Bson.Serialization.Attributes;
using System;

namespace AnalyzeResults.Errors
{
    [Serializable]
    public class TableNotReferencedError : Error
    {
        public TableNotReferencedError(int number)
            : base(ErrorType.TableNotReferenced, "Нет ссылки на таблицу", $"Таблица №{number}",
                  "Необходимо хотя бы раз сослаться на каждую таблицу в правильном формате: табл. N")
        {
            Number = number;
        }

        [BsonElement("number")]
        public int Number { get; set; }
    }
}
