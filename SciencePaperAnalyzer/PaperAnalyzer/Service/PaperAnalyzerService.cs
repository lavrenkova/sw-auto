﻿using System;
using System.IO;
using AnalyzeResults.Presentation;
using AnalyzeResults.Settings;
using TextExtractor;

namespace PaperAnalyzer.Service
{
    public class PaperAnalyzerService : IPaperAnalyzerService
    {
        public PaperAnalysisResult GetAnalyze(UploadFile file, string titles, string paperName, string refsName, ResultScoreSettings settings)
        {
            if (string.IsNullOrEmpty(file?.FileName))
            {
                throw new FileNotFoundException($"Filename is empty");
            }

            var extractor = GetTextExtractor(file.FileName);

            var text = extractor.ExtractTextFromFileStream(file.DataStream);

            var analyzer = PaperAnalyzer.Instance;

            var result = analyzer.ProcessTextWithResult(text, titles, paperName, refsName, settings);

            return result;
        }

        public ITextExtractor GetTextExtractor(string filename)
        {
            var ext = Path.GetExtension(filename);

            switch (ext)
            {
                case ".pdf":
                    return new PdfTextExtractor();

                default:
                    throw new NotImplementedException($"File type {ext} is not supported");
                
            }
        }
    }
}