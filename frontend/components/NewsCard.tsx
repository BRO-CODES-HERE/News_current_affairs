import React from 'react';

interface NewsCardProps {
  title: string;
  summary: string;
  category: string;
  source: string;
  date: string;
  url: string;
}

export default function NewsCard({ title, summary, category, source, date, url }: NewsCardProps) {
  return (
    <div className="flex flex-col bg-white dark:bg-slate-800 rounded-2xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300 ease-in-out border border-gray-100 dark:border-slate-700">
      <div className="p-6 flex-grow">
        {/* Category Tag */}
        <div className="flex justify-between items-center mb-4">
          <span className="inline-block px-3 py-1 bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300 text-xs font-semibold rounded-full uppercase tracking-wider">
            {category}
          </span>
          <span className="text-xs text-gray-500 dark:text-gray-400">
            {date}
          </span>
        </div>

        {/* Title */}
        <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-3 line-clamp-2">
          {title}
        </h2>

        {/* Summary */}
        <p className="text-gray-600 dark:text-gray-300 text-sm leading-relaxed mb-4 line-clamp-3">
          {summary}
        </p>

        {/* Footer (Source and Read More) */}
        <div className="mt-auto pt-4 border-t border-gray-100 dark:border-slate-700 flex justify-between items-center">
          <div className="flex items-center space-x-2">
            <span className="text-sm font-medium text-gray-700 dark:text-gray-300">
              {source}
            </span>
          </div>
          <a
            href={url}
            target="_blank"
            rel="noopener noreferrer"
            className="text-sm font-semibold text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 transition-colors"
          >
            Read More &rarr;
          </a>
        </div>
      </div>
    </div>
  );
}
